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

    def get_history(
        self, 
        exchange: str,
        symbol: str, 
        interval: str,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        # limit: int = None - Number of results (max: 1000)
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get top trader long/short position ratio history.
        
        Args:
            exchange: Exchange name (e.g., 'Binance')
            symbol: Symbol (e.g., 'BTCUSDT')
            interval: Interval (e.g., 'h1', 'h4', 'd1')
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
                - limit (int): Number of results (max: 1000)
        
        Returns:
            List of top trader long/short position ratio data
        """
        params = {
            'exchange': exchange,
            'symbol': symbol,
            'interval': interval,
        }
        # Add optional params from kwargs
        for key in ['startTime', 'endTime', 'limit']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/futures/top-long-short-position-ratio/history', params=params)
        return response.get('data', [])