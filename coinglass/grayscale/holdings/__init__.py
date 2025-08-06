"""
Holdings API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ..client import CoinGlassClient


class HoldingsAPI:
    """Holdings API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Holdings API with client."""
        self.client = client

    def get_list(self) -> List[Dict[str, Any]]:
        """
        Get list.
        
        Returns:
            List of data
        """
        response = self.client.get('/grayscale/holdings/list')
        return response.get('data', [])