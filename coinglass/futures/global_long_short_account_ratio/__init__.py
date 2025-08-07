"""
Global Long/Short Account Ratio API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ...client import CoinGlassClient
from ...constants import PlanLevel


class GlobalLongShortAccountRatioAPI:
    """Global Long/Short Account Ratio API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Global Long/Short Account Ratio API with client."""
        self.client = client

    def get_history(
        self,
        symbol: str,
        interval: str,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        # limit: int = None - Number of results (max: 1000)
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get historical global account ratio data.
        
        Min Plan Level: 1
        
        Args:
            symbol: Symbol (e.g., 'BTC')
            interval: Interval (5m, 15m, 30m, 1h, 4h, 1d)
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
                - limit (int): Number of results (max: 1000)
        
        Returns:
            List of global long/short account ratio data
        """
        params = {
            'symbol': symbol,
            'interval': interval,
        }
        # Add optional params from kwargs
        for key in ['startTime', 'endTime', 'limit']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/futures/global-long-short-account-ratio/history', params=params)
        return response.get('data', [])