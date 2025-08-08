"""
GlobalLongShortAccountRatio API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ...client import CoinGlassClient


class GlobalLongShortAccountRatioAPI:
    """GlobalLongShortAccountRatio API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize GlobalLongShortAccountRatio API with client."""
        self.client = client

    def get_history(self, symbol: str, interval: str) -> List[Dict[str, Any]]:
        """
        Get history.
        
        Args:
            symbol: Symbol
            interval: Interval (5m, 15m, 30m, 1h, 4h, 1d)
        
        Returns:
            List of data
        """
        params = {
            'symbol': symbol,
            'interval': interval,
        }
        response = self.client.get('/futures/global-long-short-account-ratio/history', params=params)
        return response.get('data', [])
