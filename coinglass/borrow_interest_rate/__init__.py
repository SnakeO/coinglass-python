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

    def get_history(self) -> List[Dict[str, Any]]:
        """
        Get history.
        
        Returns:
            List of data
        """
        response = self.client.get('/index/borrow-interest-rate/history')
        return response.get('data', [])