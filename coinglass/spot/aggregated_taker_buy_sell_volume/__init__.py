"""
AggregatedTakerBuySellVolume API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ...client import CoinGlassClient


class AggregatedTakerBuySellVolumeAPI:
    """AggregatedTakerBuySellVolume API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize AggregatedTakerBuySellVolume API with client."""
        self.client = client

    def get_history(
        self, 
        exchange_list: str,
        symbol: str, 
        interval: str,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        # limit: int = None - Number of results (max: 1000)
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get aggregated taker buy/sell volume history.
        
        Args:
            exchange_list: Comma-separated exchange names (e.g., 'Binance,OKX')
            symbol: Symbol (e.g., 'BTC')
            interval: Interval (e.g., 'h1', 'h4', 'd1')
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
                - limit (int): Number of results (max: 1000)
        
        Returns:
            List of aggregated taker buy/sell volume data
        """
        params = {
            'exchange_list': exchange_list,
            'symbol': symbol,
            'interval': interval,
        }
        # Add optional params from kwargs
        for key in ['startTime', 'endTime', 'limit']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/spot/aggregated-taker-buy-sell-volume/history', params=params)
        return response.get('data', [])