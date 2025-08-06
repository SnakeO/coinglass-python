"""
Liquidation API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ..client import CoinGlassClient


class LiquidationAPI:
    """Liquidation API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Liquidation API with client."""
        self.client = client
        
        from .heatmap import HeatmapAPI
        self.heatmap = HeatmapAPI(client)
        
        from .aggregated_heatmap import AggregatedHeatmapAPI
        self.aggregated_heatmap = AggregatedHeatmapAPI(client)

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
        response = self.client.get('/futures/liquidation/history', params=params)
        return response.get('data', [])
    def get_aggregated_history(self, symbol: str, interval: str) -> List[Dict[str, Any]]:
        """
        Get aggregated history.
        
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
        response = self.client.get('/futures/liquidation/aggregated-history', params=params)
        return response.get('data', [])
    def get_coin_list(self) -> List[Dict[str, Any]]:
        """
        Get coin list.
        
        Returns:
            List of data
        """
        response = self.client.get('/futures/liquidation/coin-list')
        return response.get('data', [])
    def get_exchange_list(self) -> List[Dict[str, Any]]:
        """
        Get exchange list.
        
        Returns:
            List of data
        """
        response = self.client.get('/futures/liquidation/exchange-list')
        return response.get('data', [])
    def get_order(self) -> List[Dict[str, Any]]:
        """
        Get order.
        
        Returns:
            List of data
        """
        response = self.client.get('/futures/liquidation/order')
        return response.get('data', [])
    def get_map(self, symbol: str) -> List[Dict[str, Any]]:
        """
        Get map.
        
        Args:
            symbol: Symbol
        
        Returns:
            List of data
        """
        params = {
            'symbol': symbol,
        }
        response = self.client.get('/futures/liquidation/map', params=params)
        return response.get('data', [])
    def get_aggregated_map(self, symbol: str) -> List[Dict[str, Any]]:
        """
        Get aggregated map.
        
        Args:
            symbol: Symbol
        
        Returns:
            List of data
        """
        params = {
            'symbol': symbol,
        }
        response = self.client.get('/futures/liquidation/aggregated-map', params=params)
        return response.get('data', [])