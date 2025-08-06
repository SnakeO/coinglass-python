"""
Premium API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ..client import CoinGlassClient


class PremiumAPI:
    """Premium API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Premium API with client."""
        self.client = client

    def get_history(self, symbol: Optional[str]= None) -> List[Dict[str, Any]]:
        """
        Get history.
        
        Args:
            symbol: Symbol (optional)
        
        Returns:
            List of data
        """
        params = {
            'symbol': symbol,
        }
        params = {k: v for k, v in params.items() if v is not None}
        response = self.client.get('/grayscale/premium/history', params=params)
        return response.get('data', [])