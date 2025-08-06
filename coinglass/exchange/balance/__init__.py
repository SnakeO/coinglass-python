"""
Balance API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ..client import CoinGlassClient


class BalanceAPI:
    """Balance API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Balance API with client."""
        self.client = client

    def get_list(self, symbol: str) -> List[Dict[str, Any]]:
        """
        Get list.
        
        Args:
            symbol: Symbol
        
        Returns:
            List of data
        """
        params = {
            'symbol': symbol,
        }
        response = self.client.get('/exchange/balance/list', params=params)
        return response.get('data', [])
    def get_chart(self, symbol: str) -> List[Dict[str, Any]]:
        """
        Get chart.
        
        Args:
            symbol: Symbol
        
        Returns:
            List of data
        """
        params = {
            'symbol': symbol,
        }
        response = self.client.get('/exchange/balance/chart', params=params)
        return response.get('data', [])