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

    def get_history(self, symbol: str, interval: str) -> List[Dict[str, Any]]:
        """
        Get history.
        
        Args:
            symbol: Symbol
            interval: Interval
        
        Returns:
            List of data
        """
        params = {
            'symbol': symbol,
            'interval': interval,
        }
        response = self.client.get('/futures/aggregated-taker-buy-sell-volume/history', params=params)
        return response.get('data', [])