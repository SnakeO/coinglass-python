"""
Calendar API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from .client import CoinGlassClient


class CalendarAPI:
    """Calendar API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Calendar API with client."""
        self.client = client

    def get_economic_data(self) -> List[Dict[str, Any]]:
        """
        Get economic data.
        
        Returns:
            List of data
        """
        response = self.client.get('/calendar/economic_data')
        return response.get('data', [])