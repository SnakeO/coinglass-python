"""
Futures Price API
"""
from typing import List, Dict, Any
from ...client import CoinGlassClient


class PriceAPI:
    """Futures price endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Price API with client."""
        self.client = client
    
    def get_history(self, symbol: str, interval: str) -> List[Dict[str, Any]]:
        """
        Get historical OHLC price data for a cryptocurrency.
        
        Args:
            symbol: Cryptocurrency symbol (e.g., 'BTC')
            interval: Time interval (e.g., '1m', '5m', '15m', '1h', '4h', '1d')
        
        Returns:
            List of OHLC data points
        """
        params = {
            'symbol': symbol,
            'interval': interval
        }
        response = self.client.get('/futures/price/history', params=params)
        return response.get('data', [])