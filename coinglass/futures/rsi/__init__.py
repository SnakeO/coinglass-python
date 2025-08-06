"""
Rsi API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ..client import CoinGlassClient


class RsiAPI:
    """Rsi API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Rsi API with client."""
        self.client = client

    def get_list(self) -> List[Dict[str, Any]]:
        """
        Get list.
        
        Returns:
            List of data
        """
        response = self.client.get('/futures/rsi/list')
        return response.get('data', [])