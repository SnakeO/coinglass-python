"""
CoinGlass API Exceptions
Custom exception classes for the CoinGlass API client
"""
from typing import Optional, Dict, Any


class CoinGlassException(Exception):
    """Base exception for all CoinGlass-related errors."""
    pass


class CoinGlassAPIError(CoinGlassException):
    """Exception raised for CoinGlass API errors."""
    
    def __init__(self, code: str, message: str, response: Optional[Dict[str, Any]] = None):
        """
        Initialize API error.
        
        Args:
            code: Error code from API
            message: Error message
            response: Full API response
        """
        self.code = code
        self.message = message
        self.response = response
        super().__init__(f"CoinGlass API Error [{code}]: {message}")


class CoinGlassAuthenticationError(CoinGlassException):
    """Raised when API authentication fails."""
    pass


class CoinGlassRateLimitError(CoinGlassException):
    """Raised when API rate limit is exceeded."""
    
    def __init__(self, retry_after: Optional[int] = None):
        """
        Initialize rate limit error.
        
        Args:
            retry_after: Seconds to wait before retrying
        """
        self.retry_after = retry_after
        message = "Rate limit exceeded"
        if retry_after:
            message += f". Retry after {retry_after} seconds"
        super().__init__(message)


class CoinGlassValidationError(CoinGlassException):
    """Raised when request validation fails."""
    pass


class CoinGlassNetworkError(CoinGlassException):
    """Raised for network-related errors."""
    pass


class CoinGlassTimeoutError(CoinGlassNetworkError):
    """Raised when a request times out."""
    pass