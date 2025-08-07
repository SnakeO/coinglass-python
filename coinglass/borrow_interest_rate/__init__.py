"""
BorrowInterestRate API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ..client import CoinGlassClient


class BorrowInterestRateAPI:
    """BorrowInterestRate API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize BorrowInterestRate API with client."""
        self.client = client

    def get_history(self, symbol: str, **kwargs) -> List[Dict[str, Any]]:
        """
        Get history.
        
        Args:
            symbol: Symbol (e.g., 'BTC')
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of data
        """
        params = {'symbol': symbol}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        response = self.client.get('/borrow-interest-rate/history', params=params)
        return response.get('data', [])