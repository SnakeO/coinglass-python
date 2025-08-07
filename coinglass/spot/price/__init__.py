"""
Price API for CoinGlass Spot
"""
from typing import Optional, List, Dict, Any
from ...client import CoinGlassClient
from ...constants import PlanLevel


class PriceAPI:
    """Spot Price API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Price API with client."""
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
        Get historical OHLC price data for spot markets.
        
        Plan Availability: 
        - Hobbyist: Intervals ≥ 4h only
        - Startup: Intervals ≥ 30m
        - Standard+: No interval restrictions
        
        Args:
            symbol: Symbol (e.g., 'BTC/USDT')
            interval: Interval (1m, 3m, 5m, 15m, 30m, 1h, 4h, 6h, 8h, 12h, 1d, 1w)
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
                - limit (int): Number of results (max: 1000)
        
        Returns:
            List of spot price history OHLC data
        """
        params = {
            'symbol': symbol,
            'interval': interval,
        }
        # Add optional params from kwargs
        for key in ['startTime', 'endTime', 'limit']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/spot/price/history', params=params)
        return response.get('data', [])