"""
RSI API for CoinGlass Futures
"""
from typing import Optional, List, Dict, Any
from ...client import CoinGlassClient
from ...constants import PlanTier, CacheTime


class RsiAPI:
    """Futures RSI API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize RSI API with client."""
        self.client = client

    def get_list(self) -> List[Dict[str, Any]]:
        """
        Get RSI values across multiple timeframes.
        
        Plan Availability: Standard+
        Cache: Every 10 seconds
        
        Returns:
            List of RSI data across timeframes
        """
        response = self.client.get('/futures/rsi-list')
        return response.get('data', [])