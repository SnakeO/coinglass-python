"""
Orderbook API for CoinGlass Spot
"""
from typing import Optional, List, Dict, Any
from ...client import CoinGlassClient


class OrderbookAPI:
    """Spot Orderbook API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Orderbook API with client."""
        self.client = client

    def get_ask_bids_history(
        self, 
        exchange: str,
        symbol: str, 
        interval: str,
        # Optional parameters
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get historical ask/bid data for spot.
        
        Args:
            exchange: Exchange name (e.g., 'Binance')
            symbol: Symbol (e.g., 'BTCUSDT')
            interval: Interval (1m, 3m, 5m, 15m, 30m, 1h, 4h, 6h, 8h, 12h, 1d, 1w)
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
                - limit (int): Number of results (max: 1000)
        
        Returns:
            List of ask/bid history data
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
        
        response = self.client.get('/spot/orderbook/ask-bids-history', params=params)
        return response.get('data', [])
    
    def get_aggregated_ask_bids_history(
        self, 
        exchange_list: str,
        symbol: str, 
        interval: str,
        # Optional parameters
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get aggregated ask/bid data across exchanges.
        
        Args:
            exchange_list: Comma-separated exchange names (e.g., 'Binance,OKX')
            symbol: Symbol (e.g., 'BTC')
            interval: Interval (e.g., 'h1', 'h4', 'd1')
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
                - limit (int): Number of results (max: 1000)
        
        Returns:
            List of aggregated ask/bid history data
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
        
        response = self.client.get('/spot/orderbook/aggregated-ask-bids-history', params=params)
        return response.get('data', [])
    
    def get_history(
        self, 
        symbol: str, 
        ex: str,
        # Optional parameters
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get historical orderbook data.
        
        Args:
            symbol: Symbol (e.g., 'BTC/USDT')
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
        
        response = self.client.get('/spot/orderbook/history', params=params)
        return response.get('data', [])
    
    def get_large_limit_order(
        self, 
        symbol: str, 
        ex: str
    ) -> List[Dict[str, Any]]:
        """
        Get current large limit orders in spot markets.
        
        Min Plan Level: 3 (Standard+)
        
        Args:
            symbol: Symbol (e.g., 'BTC/USDT')
            ex: Exchange name (e.g., 'Binance')
        
        Returns:
            List of large limit orders
        """
        params = {
            'symbol': symbol,
            'ex': ex,
        }
        response = self.client.get('/spot/orderbook/large-limit-order', params=params)
        return response.get('data', [])
    
    def get_large_limit_order_history(
        self, 
        symbol: str, 
        ex: str,
        # Optional parameters
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get historical large limit orders for spot markets.
        
        Min Plan Level: 3 (Standard+)
        
        Args:
            symbol: Symbol (e.g., 'BTC/USDT')
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
        
        response = self.client.get('/spot/orderbook/large-limit-order-history', params=params)
        return response.get('data', [])