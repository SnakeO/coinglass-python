"""
Liquidation API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ...client import CoinGlassClient
from ...constants import PlanLevel, CacheTime


class LiquidationAPI:
    """Liquidation API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Liquidation API with client."""
        self.client = client
        
        from .heatmap import HeatmapAPI
        self.heatmap = HeatmapAPI(client)
        
        from .aggregated_heatmap import AggregatedHeatmapAPI
        self.aggregated_heatmap = AggregatedHeatmapAPI(client)

    def get_history(
        self,
        ex: str,
        symbol: str,
        interval: str
    ) -> List[Dict[str, Any]]:
        """
        Get historical liquidation data for pairs.
        
        Min Plan Level: 1
        
        Args:
            ex: Exchange name (e.g., 'Binance')
            symbol: Symbol (e.g., 'BTCUSDT')
            interval: Interval (1m, 3m, 5m, 15m, 30m, 1h, 4h, 6h, 8h, 12h, 1d, 1w)
        
        Returns:
            List of liquidation history data
        """
        params = {
            'ex': ex,
            'symbol': symbol,
            'interval': interval,
        }
        response = self.client.get('/futures/liquidation/history', params=params)
        return response.get('data', [])
    
    def get_aggregated_history(
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
        Get aggregated liquidation data across exchanges.
        
        Min Plan Level: 1
        
        Args:
            symbol: Symbol (e.g., 'BTC')
            interval: Interval (1m, 3m, 5m, 15m, 30m, 1h, 4h, 6h, 8h, 12h, 1d, 1w)
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
                - limit (int): Number of results (max: 1000)
        
        Returns:
            List of aggregated liquidation data
        """
        params = {
            'symbol': symbol,
            'interval': interval,
        }
        # Add optional params from kwargs
        for key in ['startTime', 'endTime', 'limit']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/futures/liquidation/aggregated-history', params=params)
        return response.get('data', [])
    
    def get_coin_list(
        self,
        # Optional parameters (can be passed as kwargs):
        # ex: str = None - Exchange name
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get liquidation data grouped by coin.
        
        Min Plan Level: 2
        
        Args:
            **kwargs: Optional parameters:
                - ex (str): Exchange name
        
        Returns:
            List of liquidation data by coin
        """
        params = {}
        if 'ex' in kwargs:
            params['ex'] = kwargs['ex']
        
        response = self.client.get('/futures/liquidation/coin-list', params=params if params else None)
        return response.get('data', [])
    
    def get_exchange_list(
        self,
        # Optional parameters (can be passed as kwargs):
        # symbol: str = None - Symbol
        # ex: str = None - Exchange name
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get current liquidation data by exchange.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - symbol (str): Symbol (e.g., 'BTC')
                - ex (str): Exchange name
        
        Returns:
            List of liquidation data by exchange
        """
        params = {}
        for key in ['symbol', 'ex']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/futures/liquidation/exchange-list', params=params if params else None)
        return response.get('data', [])
    
    def get_order(
        self,
        ex: str,
        symbol: str
    ) -> List[Dict[str, Any]]:
        """
        Get recent liquidation orders.
        
        Min Plan Level: 3
        Cache: Every 1 second
        
        Args:
            ex: Exchange name (e.g., 'Binance')
            symbol: Symbol (e.g., 'BTCUSDT')
        
        Returns:
            List of recent liquidation orders
        """
        params = {
            'ex': ex,
            'symbol': symbol
        }
        response = self.client.get('/futures/liquidation/order', params=params)
        return response.get('data', [])
    
    def get_map(
        self,
        ex: str,
        symbol: str
    ) -> List[Dict[str, Any]]:
        """
        Get liquidation map visualization data.
        
        Min Plan Level: 4
        
        Args:
            ex: Exchange name (e.g., 'Binance')
            symbol: Symbol (e.g., 'BTCUSDT')
        
        Returns:
            List of liquidation map data
        """
        params = {
            'ex': ex,
            'symbol': symbol,
        }
        response = self.client.get('/futures/liquidation/map', params=params)
        return response.get('data', [])
    
    def get_aggregated_map(
        self,
        symbol: str
    ) -> List[Dict[str, Any]]:
        """
        Get aggregated liquidation map across exchanges.
        
        Min Plan Level: 4
        
        Args:
            symbol: Symbol (e.g., 'BTC')
        
        Returns:
            List of aggregated liquidation map data
        """
        params = {
            'symbol': symbol,
        }
        response = self.client.get('/futures/liquidation/aggregated-map', params=params)
        return response.get('data', [])