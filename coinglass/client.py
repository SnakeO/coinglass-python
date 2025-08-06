"""
CoinGlass API Client
Base client for interacting with the CoinGlass API v4
"""
import os
import time
import logging
from typing import Optional, Dict, Any, Union
from urllib.parse import urljoin, urlencode
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from .exceptions import CoinGlassAPIError

logger = logging.getLogger(__name__)


class CoinGlassClient:
    """
    Base client for CoinGlass API v4
    
    Handles authentication, request formatting, rate limiting, and error handling.
    """
    
    BASE_URL = "https://open-api-v4.coinglass.com/api"
    DEFAULT_TIMEOUT = 30
    MAX_RETRIES = 3
    RETRY_BACKOFF_FACTOR = 0.5
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: int = DEFAULT_TIMEOUT,
        max_retries: int = MAX_RETRIES,
        session: Optional[requests.Session] = None
    ):
        """
        Initialize CoinGlass API client.
        
        Args:
            api_key: Your CoinGlass API key. If not provided, will look for CG_API_KEY env var.
            base_url: Override the default API base URL
            timeout: Request timeout in seconds
            max_retries: Maximum number of retry attempts for failed requests
            session: Optional requests.Session to use for HTTP requests
        """
        self.api_key = api_key or os.environ.get('CG_API_KEY')
        if not self.api_key:
            raise ValueError(
                "API key is required. Provide it via api_key parameter or CG_API_KEY environment variable."
            )
        
        self.base_url = base_url or self.BASE_URL
        self.timeout = timeout
        self.max_retries = max_retries
        
        # Setup session with retry strategy
        if session is None:
            self.session = requests.Session()
            retry_strategy = Retry(
                total=max_retries,
                backoff_factor=self.RETRY_BACKOFF_FACTOR,
                status_forcelist=[429, 500, 502, 503, 504],
                allowed_methods=["GET", "POST", "PUT", "DELETE"]
            )
            adapter = HTTPAdapter(max_retries=retry_strategy)
            self.session.mount("http://", adapter)
            self.session.mount("https://", adapter)
        else:
            self.session = session
        
        # Set default headers
        self.session.headers.update({
            'CG-API-KEY': self.api_key,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    
    def _make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Make an HTTP request to the CoinGlass API.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path (will be joined with base_url)
            params: Query parameters
            data: Request body data (for POST/PUT requests)
            **kwargs: Additional arguments to pass to requests
        
        Returns:
            Parsed JSON response
        
        Raises:
            CoinGlassAPIError: If the API returns an error
            requests.RequestException: For network-related errors
        """
        # Build full URL
        if endpoint.startswith('/'):
            endpoint = endpoint[1:]
        url = urljoin(self.base_url + '/', endpoint)
        
        # Clean up parameters - remove None values
        if params:
            params = {k: v for k, v in params.items() if v is not None}
        
        # Set timeout if not provided
        if 'timeout' not in kwargs:
            kwargs['timeout'] = self.timeout
        
        # Log the request
        logger.debug(f"{method} {url} with params: {params}")
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=data,
                **kwargs
            )
            
            # Check for rate limiting
            if response.status_code == 429:
                retry_after = int(response.headers.get('Retry-After', 60))
                logger.warning(f"Rate limited. Waiting {retry_after} seconds...")
                time.sleep(retry_after)
                # Retry the request
                response = self.session.request(
                    method=method,
                    url=url,
                    params=params,
                    json=data,
                    **kwargs
                )
            
            # Raise exception for bad status codes
            response.raise_for_status()
            
            # Parse JSON response
            result = response.json()
            
            # Check for API-level errors
            if result.get('code') != '0':
                raise CoinGlassAPIError(
                    code=result.get('code'),
                    message=result.get('msg', 'Unknown error'),
                    response=result
                )
            
            return result
            
        except requests.exceptions.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON response: {response.text}")
            raise CoinGlassAPIError(
                code='JSON_ERROR',
                message=f"Invalid JSON response: {str(e)}",
                response={'raw': response.text}
            )
        except requests.RequestException as e:
            logger.error(f"Request failed: {str(e)}")
            raise
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        """
        Make a GET request to the API.
        
        Args:
            endpoint: API endpoint path
            params: Query parameters
            **kwargs: Additional arguments to pass to requests
        
        Returns:
            Parsed JSON response
        """
        return self._make_request('GET', endpoint, params=params, **kwargs)
    
    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        """
        Make a POST request to the API.
        
        Args:
            endpoint: API endpoint path
            data: Request body data
            **kwargs: Additional arguments to pass to requests
        
        Returns:
            Parsed JSON response
        """
        return self._make_request('POST', endpoint, data=data, **kwargs)
    
    def close(self):
        """Close the underlying session."""
        self.session.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()