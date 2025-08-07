"""
TopLongShortPositionRatio API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ...client import CoinGlassClient


class TopLongShortPositionRatioAPI:
    """TopLongShortPositionRatio API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize TopLongShortPositionRatio API with client."""
        self.client = client

    def get_history(self, symbol: str, exchange: str, interval: str) -> List[Dict[str, Any]]:
        """
        Get history.
        
        Args:
            symbol: Symbol\n            exchange: Exchange name
            interval: Interval
        
        Returns:
            List of data
        """
        params = {
            'symbol': symbol,
            'exchange': exchange,
            'interval': interval,
        }
        response = self.client.get('/futures/top-long-short-position-ratio/history', params=params)
        return response.get('data', [])