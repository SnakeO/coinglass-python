"""
TakerBuySellVolume API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ...client import CoinGlassClient


class TakerBuySellVolumeAPI:
    """TakerBuySellVolume API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize TakerBuySellVolume API with client."""
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
        response = self.client.get('/futures/taker-buy-sell-volume/history', params=params)
        return response.get('data', [])
    def get_exchange_list(self, symbol: str) -> List[Dict[str, Any]]:
        """
        Get exchange list.
        
        Args:
            symbol: Symbol
        
        Returns:
            List of data
        """
        params = {
            'symbol': symbol,
        }
        response = self.client.get('/futures/taker-buy-sell-volume/exchange-list', params=params)
        return response.get('data', [])