"""
Futures Open Interest API
"""
from typing import List, Dict, Any, Optional
from ...client import CoinGlassClient


class OpenInterestAPI:
    """Futures open interest endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Open Interest API with client."""
        self.client = client
    
    def get_history(self, symbol: str, interval: str) -> List[Dict[str, Any]]:
        """
        Get futures open interest history in OHLC format.
        
        Args:
            symbol: Futures instrument identifier (e.g., 'BTCUSDT_PERP')
            interval: Candlestick interval (e.g., '1h', '4h', '1d')
        
        Returns:
            List of open interest OHLC data
        """
        params = {
            'symbol': symbol,
            'interval': interval
        }
        response = self.client.get('/futures/open-interest/history', params=params)
        return response.get('data', [])
    
    def get_aggregated_history(self, symbol: str, interval: str) -> List[Dict[str, Any]]:
        """
        Get aggregated futures open interest OHLC data across all exchanges.
        
        Args:
            symbol: Cryptocurrency symbol (e.g., 'BTC')
            interval: Candlestick interval (e.g., '4h', '1d')
        
        Returns:
            List of aggregated open interest OHLC data
        """
        params = {
            'symbol': symbol,
            'interval': interval
        }
        response = self.client.get('/futures/open-interest/aggregated-history', params=params)
        return response.get('data', [])
    
    def get_aggregated_stablecoin_margin_history(self, symbol: str, interval: str) -> List[Dict[str, Any]]:
        """
        Get aggregated open interest OHLC data for stablecoin-margined futures.
        
        Args:
            symbol: Cryptocurrency symbol (e.g., 'BTC')
            interval: Candlestick interval
        
        Returns:
            List of stablecoin-margined OI OHLC data
        """
        params = {
            'symbol': symbol,
            'interval': interval
        }
        response = self.client.get('/futures/open-interest/aggregated-stablecoin-margin-history', params=params)
        return response.get('data', [])
    
    def get_aggregated_coin_margin_history(self, symbol: str, interval: str) -> List[Dict[str, Any]]:
        """
        Get aggregated open interest OHLC data for coin-margined futures.
        
        Args:
            symbol: Cryptocurrency symbol (e.g., 'BTC')
            interval: Candlestick interval
        
        Returns:
            List of coin-margined OI OHLC data
        """
        params = {
            'symbol': symbol,
            'interval': interval
        }
        response = self.client.get('/futures/open-interest/aggregated-coin-margin-history', params=params)
        return response.get('data', [])
    
    def get_exchange_list(self, symbol: str) -> Dict[str, Any]:
        """
        Get current open interest for a coin, broken down by exchange.
        
        Args:
            symbol: Cryptocurrency symbol (e.g., 'BTC')
        
        Returns:
            Open interest data by exchange
        """
        params = {'symbol': symbol}
        response = self.client.get('/futures/open-interest/exchange-list', params=params)
        return response.get('data', {})
    
    def get_exchange_history_chart(self, symbol: str) -> Dict[str, Any]:
        """
        Get historical open interest distribution across exchanges for charting.
        
        Args:
            symbol: Cryptocurrency symbol (e.g., 'BTC')
        
        Returns:
            Historical OI distribution data
        """
        params = {'symbol': symbol}
        response = self.client.get('/futures/open-interest/exchange-history-chart', params=params)
        return response.get('data', {})