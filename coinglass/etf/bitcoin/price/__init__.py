"""
Price API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ....client import CoinGlassClient


class PriceAPI:
    """Price API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Price API with client."""
        self.client = client

    def get_history(self) -> List[Dict[str, Any]]:
        """
        Get history.
        
        Returns:
            List of data
        """
        response = self.client.get('/etf/bitcoin/price/history')
        return response.get('data', [])