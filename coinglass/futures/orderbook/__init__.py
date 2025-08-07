"""
Orderbook API for CoinGlass Futures
"""
from typing import Optional, List, Dict, Any
from ...client import CoinGlassClient
from ...constants import PlanLevel


class OrderbookAPI:
    """Futures Orderbook API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Orderbook API with client."""
        self.client = client

    def get_ask_bids_history(
        self,
        symbol: str,
        ex: str,
        interval: str,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        # limit: int = None - Number of results (max: 1000)
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get historical ask/bid data for futures.
        
        Min Plan Level: 1
        
        Args:
            symbol: Symbol (e.g., 'BTCUSDT')
            ex: Exchange name (e.g., 'Binance')
            interval: Interval (1m, 3m, 5m, 15m, 30m, 1h, 4h, 6h, 8h, 12h, 1d, 1w)
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
                - limit (int): Number of results (max: 1000)
        
        Returns:
            List of ask/bid history data
        """
        params = {
            'symbol': symbol,
            'ex': ex,
            'interval': interval,
        }
        # Add optional params from kwargs
        for key in ['startTime', 'endTime', 'limit']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/futures/orderbook/ask-bids-history', params=params)
        return response.get('data', [])
    
    def get_aggregated_ask_bids_history(
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
        Get aggregated ask/bid data across exchanges.
        
        Min Plan Level: 1
        
        Args:
            symbol: Symbol (e.g., 'BTC')
            interval: Interval (1m, 3m, 5m, 15m, 30m, 1h, 4h, 6h, 8h, 12h, 1d, 1w)
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
                - limit (int): Number of results (max: 1000)
        
        Returns:
            List of aggregated ask/bid history data
        """
        params = {
            'symbol': symbol,
            'interval': interval,
        }
        # Add optional params from kwargs
        for key in ['startTime', 'endTime', 'limit']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/futures/orderbook/aggregated-ask-bids-history', params=params)
        return response.get('data', [])
    
    def get_history(
        self,
        symbol: str,
        ex: str,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        # limit: int = None - Number of results (max: 1000)
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get historical orderbook data.
        
        Min Plan Level: 1
        
        Args:
            symbol: Symbol (e.g., 'BTCUSDT')
            ex: Exchange name (e.g., 'Binance')
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
                - limit (int): Number of results (max: 1000)
        
        Returns:
            List of orderbook history data
        """
        params = {
            'symbol': symbol,
            'ex': ex,
        }
        # Add optional params from kwargs
        for key in ['startTime', 'endTime', 'limit']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/futures/orderbook/history', params=params)
        return response.get('data', [])
    
    def get_large_limit_order(
        self,
        symbol: str,
        ex: str
    ) -> List[Dict[str, Any]]:
        """
        Get current large limit orders in futures.
        
        Min Plan Level: 3
        
        Args:
            symbol: Symbol (e.g., 'BTCUSDT')
            ex: Exchange name (e.g., 'Binance')
        
        Returns:
            List of large limit orders
        """
        params = {
            'symbol': symbol,
            'ex': ex,
        }
        response = self.client.get('/futures/orderbook/large-limit-order', params=params)
        return response.get('data', [])
    
    def get_large_limit_order_history(
        self,
        symbol: str,
        ex: str,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get historical large limit orders for futures.
        
        Min Plan Level: 3
        
        Args:
            symbol: Symbol (e.g., 'BTCUSDT')
            ex: Exchange name (e.g., 'Binance')
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of historical large limit orders
        """
        params = {
            'symbol': symbol,
            'ex': ex,
        }
        # Add optional params from kwargs
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/futures/orderbook/large-limit-order-history', params=params)
        return response.get('data', [])