"""
Option API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ..client import CoinGlassClient
from ..constants import PlanLevel, CacheTime


class OptionAPI:
    """Option API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Option API with client."""
        self.client = client

    def get_max_pain(
        self,
        symbol: str,
        exchange: str,
        # Optional parameters (can be passed as kwargs):
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get options max pain calculation.
        
        Min Plan Level: 1
        Cache: Every 1 minute
        
        Args:
            symbol: Symbol (e.g., 'BTC')
            exchange: Exchange name (e.g., 'Deribit')
            **kwargs: Optional parameters
        
        Returns:
            List of max pain data
        """
        params = {
            'symbol': symbol,
            'exchange': exchange
        }
        # Add optional params from kwargs
        for key in kwargs:
            params[key] = kwargs[key]
        
        response = self.client.get('/option/max-pain', params=params)
        return response.get('data', [])
    
    def get_info(
        self,
        # Optional parameters (can be passed as kwargs):
        # symbol: str = 'BTC' - Symbol (defaults to BTC)
        **kwargs
    ) -> Dict[str, Any]:
        """
        Get options market overview info.
        
        Min Plan Level: 1
        Cache: Every 30 seconds
        
        Args:
            **kwargs: Optional parameters:
                - symbol (str): Symbol (default: 'BTC')
        
        Returns:
            Options market info data dictionary
        """
        params = {}
        if 'symbol' in kwargs:
            params['symbol'] = kwargs['symbol']
        
        response = self.client.get('/option/info', params=params if params else None)
        return response.get('data', {})
    
    def get_exchange_oi_history(
        self,
        symbol: str,
        unit: str,
        range: str,
        # Optional parameters (can be passed as kwargs):
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get historical open interest by exchange for options.
        
        Min Plan Level: 1
        
        Args:
            symbol: Symbol (e.g., 'BTC')
            unit: Unit type (e.g., 'USD', 'BTC')
            range: Time range (e.g., '1h', '4h', '1d')
            **kwargs: Optional parameters
        
        Returns:
            List of OI history data by exchange
        """
        params = {
            'symbol': symbol,
            'unit': unit,
            'range': range,
        }
        # Add optional params from kwargs
        for key in kwargs:
            params[key] = kwargs[key]
        
        response = self.client.get('/option/exchange-oi-history', params=params)
        return response.get('data', [])
    
    def get_exchange_vol_history(
        self,
        symbol: str,
        time_type: str,
        # Optional parameters (can be passed as kwargs):
        # currency: str = None - Currency type
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get historical volume by exchange for options.
        
        Min Plan Level: 1
        
        Args:
            symbol: Symbol (e.g., 'BTC')
            time_type: Time type for aggregation
            **kwargs: Optional parameters:
                - currency (str): Currency type
        
        Returns:
            List of volume history data by exchange
        """
        params = {
            'symbol': symbol,
            'time_type': time_type,
        }
        if 'currency' in kwargs:
            params['currency'] = kwargs['currency']
        
        response = self.client.get('/option/exchange-vol-history', params=params)
        return response.get('data', [])