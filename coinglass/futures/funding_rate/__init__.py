"""
Funding Rate API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ...client import CoinGlassClient
from ...constants import PlanLevel, CacheTime, Interval


class FundingRateAPI:
    """Funding Rate API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Funding Rate API with client."""
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
        Get historical funding rate data.
        
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
            List of funding rate history data
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
        
        response = self.client.get('/futures/funding-rate/history', params=params)
        return response.get('data', [])
    
    def get_oi_weight_history(
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
        Get open interest weighted funding rate history.
        
        Min Plan Level: 1
        
        Args:
            symbol: Symbol (e.g., 'BTC')
            interval: Interval (1m, 3m, 5m, 15m, 30m, 1h, 4h, 6h, 8h, 12h, 1d, 1w)
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
                - limit (int): Number of results (max: 1000)
        
        Returns:
            List of OI-weighted funding rate data
        """
        params = {
            'symbol': symbol,
            'interval': interval,
        }
        # Add optional params from kwargs
        for key in ['startTime', 'endTime', 'limit']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/futures/funding-rate/oi-weight-history', params=params)
        return response.get('data', [])
    
    def get_vol_weight_history(
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
        Get volume weighted funding rate history.
        
        Min Plan Level: 1
        
        Args:
            symbol: Symbol (e.g., 'BTC')
            interval: Interval (1m, 3m, 5m, 15m, 30m, 1h, 4h, 6h, 8h, 12h, 1d, 1w)
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
                - limit (int): Number of results (max: 1000)
        
        Returns:
            List of volume-weighted funding rate data
        """
        params = {
            'symbol': symbol,
            'interval': interval,
        }
        # Add optional params from kwargs
        for key in ['startTime', 'endTime', 'limit']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/futures/funding-rate/vol-weight-history', params=params)
        return response.get('data', [])
    
    def get_exchange_list(
        self,
        # Optional parameters (can be passed as kwargs):
        # symbol: str = None - Symbol
        # ex: str = None - Exchange name
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get current funding rates by exchange.
        
        Min Plan Level: 1
        Cache: Every 20 seconds
        
        Args:
            **kwargs: Optional parameters:
                - symbol (str): Symbol (e.g., 'BTC')
                - ex (str): Exchange name
        
        Returns:
            List of funding rates by exchange
        """
        params = {}
        # Add optional params from kwargs
        for key in ['symbol', 'ex']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/futures/funding-rate/exchange-list', params=params if params else None)
        return response.get('data', [])
    
    def get_accumulated_exchange_list(
        self,
        # Optional parameters (can be passed as kwargs):
        # symbol: str = None - Symbol
        # ex: str = None - Exchange name
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get accumulated funding rate data by exchange.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - symbol (str): Symbol (e.g., 'BTC')
                - ex (str): Exchange name
        
        Returns:
            List of accumulated funding rates by exchange
        """
        params = {}
        # Add optional params from kwargs
        for key in ['symbol', 'ex']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/futures/funding-rate/accumulated-exchange-list', params=params if params else None)
        return response.get('data', [])
    
    def get_arbitrage(
        self,
        symbol: str,
        # Optional parameters (can be passed as kwargs):
        # minSpread: float = None - Minimum spread threshold
        # limit: int = None - Number of results (max: 100)
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get funding rate arbitrage opportunities.
        
        Min Plan Level: 3
        Cache: Every 30 seconds
        
        Args:
            symbol: Symbol (e.g., 'BTC')
            **kwargs: Optional parameters:
                - minSpread (float): Minimum spread threshold
                - limit (int): Number of results (max: 100)
        
        Returns:
            List of arbitrage opportunities
        """
        params = {'symbol': symbol}
        # Add optional params from kwargs
        for key in ['minSpread', 'limit']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/futures/funding-rate-arbitrage', params=params)
        return response.get('data', [])