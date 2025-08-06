"""
NetAssets API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ...client import CoinGlassClient


class NetAssetsAPI:
    """NetAssets API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize NetAssets API with client."""
        self.client = client

    def get_history(self) -> List[Dict[str, Any]]:
        """
        Get history.
        
        Returns:
            List of data
        """
        response = self.client.get('/etf/ethereum/net_assets/history')
        return response.get('data', [])