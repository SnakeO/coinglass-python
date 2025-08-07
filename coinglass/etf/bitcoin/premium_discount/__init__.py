"""
PremiumDiscount API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ....client import CoinGlassClient


class PremiumDiscountAPI:
    """PremiumDiscount API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize PremiumDiscount API with client."""
        self.client = client

    def get_history(self) -> List[Dict[str, Any]]:
        """
        Get history.
        
        Returns:
            List of data
        """
        response = self.client.get('/etf/bitcoin/premium-discount/history')
        return response.get('data', [])