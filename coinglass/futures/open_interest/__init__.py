"""
Futures Open Interest API
"""
from typing import List, Dict, Any, Optional
from ...client import CoinGlassClient
from ...constants import PlanLevel, CacheTime, Interval


class OpenInterestAPI:
    """Futures open interest endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Open Interest API with client."""
        self.client = client
    
    def get_history(
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
        Get futures open interest history in OHLC format.
        
        Min Plan Level: 1
        
        Args:
            symbol: Futures instrument identifier (e.g., 'BTCUSDT_PERP')
            exchange: Exchange name (e.g., 'Binance')
            interval: Candlestick interval (1m, 3m, 5m, 15m, 30m, 1h, 4h, 6h, 8h, 12h, 1d, 1w)
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
                - limit (int): Number of results (max: 1000)
        
        Returns:
            List of open interest OHLC data
        """
        params = {
            'symbol': symbol,
            'exchange': exchange,
            'interval': interval
        }
        # Add optional params from kwargs
        for key in ['startTime', 'endTime', 'limit']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/futures/open-interest/history', params=params)
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
        Get aggregated futures open interest OHLC data across all exchanges.
        
        Min Plan Level: 1
        
        Args:
            symbol: Cryptocurrency symbol (e.g., 'BTC')
            interval: Candlestick interval (1m, 3m, 5m, 15m, 30m, 1h, 4h, 6h, 8h, 12h, 1d, 1w)
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
                - limit (int): Number of results (max: 1000)
        
        Returns:
            List of aggregated open interest OHLC data
        """
        params = {
            'symbol': symbol,
            'interval': interval
        }
        # Add optional params from kwargs
        for key in ['startTime', 'endTime', 'limit']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/futures/open-interest/aggregated-history', params=params)
        return response.get('data', [])
    
    def get_aggregated_stablecoin_margin_history(
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
        Get aggregated open interest OHLC data for stablecoin-margined futures.
        
        Min Plan Level: 1
        
        Args:
            symbol: Cryptocurrency symbol (e.g., 'BTC')
            interval: Candlestick interval (1m, 3m, 5m, 15m, 30m, 1h, 4h, 6h, 8h, 12h, 1d, 1w)
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
                - limit (int): Number of results (max: 1000)
        
        Returns:
            List of stablecoin-margined OI OHLC data
        """
        params = {
            'symbol': symbol,
            'interval': interval
        }
        # Add optional params from kwargs
        for key in ['startTime', 'endTime', 'limit']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/futures/open-interest/aggregated-stablecoin-history', params=params)
        return response.get('data', [])
    
    def get_aggregated_coin_margin_history(
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
        Get aggregated open interest OHLC data for coin-margined futures.
        
        Min Plan Level: 1
        
        Args:
            symbol: Cryptocurrency symbol (e.g., 'BTC')
            interval: Candlestick interval (1m, 3m, 5m, 15m, 30m, 1h, 4h, 6h, 8h, 12h, 1d, 1w)
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
                - limit (int): Number of results (max: 1000)
        
        Returns:
            List of coin-margined OI OHLC data
        """
        params = {
            'symbol': symbol,
            'interval': interval
        }
        # Add optional params from kwargs
        for key in ['startTime', 'endTime', 'limit']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/futures/open-interest/aggregated-coin-margin-history', params=params)
        return response.get('data', [])
    
    def get_exchange_list(
        self,
        # Optional parameters (can be passed as kwargs):
        # symbol: str = None - Cryptocurrency symbol
        # ex: str = None - Exchange name
        **kwargs
    ) -> Dict[str, Any]:
        """
        Get current open interest for a coin, broken down by exchange.
        
        Min Plan Level: 1
        Cache: Every 10 seconds
        
        Args:
            **kwargs: Optional parameters:
                - symbol (str): Cryptocurrency symbol (e.g., 'BTC')
                - ex (str): Exchange name
        
        Returns:
            Open interest data by exchange
        """
        params = {}
        # Add optional params from kwargs
        for key in ['symbol', 'ex']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/futures/open-interest/exchange-list', params=params if params else None)
        return response.get('data', {})
    
    def get_exchange_history_chart(
        self,
        symbol: str,
        interval: str
    ) -> Dict[str, Any]:
        """
        Get historical open interest distribution across exchanges for charting.
        
        Min Plan Level: 1
        
        Args:
            symbol: Cryptocurrency symbol (e.g., 'BTC')
            interval: Interval (1h, 4h, 1d)
        
        Returns:
            Historical OI distribution data
        """
        params = {
            'symbol': symbol,
            'interval': interval
        }
        response = self.client.get('/futures/open-interest/exchange-history-chart', params=params)
        return response.get('data', {})