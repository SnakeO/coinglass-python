"""
Balance API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ...client import CoinGlassClient
from ...constants import PlanLevel


class BalanceAPI:
    """Balance API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Balance API with client."""
        self.client = client

    def get_list(
        self,
        symbol: str,
        # Optional parameters (can be passed as kwargs):
        # exchange: str = None - Specific exchange name
        # limit: int = None - Number of results to return
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get exchange balance list for a symbol.
        
        Min Plan Level: 1
        
        Args:
            symbol: Symbol (e.g., 'BTC', 'ETH')
            **kwargs: Optional parameters:
                - exchange (str): Specific exchange name
                - limit (int): Number of results to return
        
        Returns:
            List of exchange balance data
        """
        params = {
            'symbol': symbol,
        }
        # Add optional params from kwargs
        for key in ['exchange', 'limit']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/exchange/balance/list', params=params)
        return response.get('data', [])
    def get_chart(
        self,
        symbol: str,
        # Optional parameters (can be passed as kwargs):
        # exchange: str = None - Specific exchange name
        # interval: str = None - Time interval for chart data
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get exchange balance chart data.
        
        Min Plan Level: 1
        
        Args:
            symbol: Symbol (e.g., 'BTC', 'ETH')
            **kwargs: Optional parameters:
                - exchange (str): Specific exchange name
                - interval (str): Time interval for chart data
        
        Returns:
            List of balance chart data
        """
        params = {
            'symbol': symbol,
        }
        # Add optional params from kwargs
        for key in ['exchange', 'interval']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/exchange/balance/chart', params=params)
        return response.get('data', [])