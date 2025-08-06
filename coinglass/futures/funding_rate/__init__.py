"""
Futures Funding Rate API
"""
from typing import List, Dict, Any
from ...client import CoinGlassClient


class FundingRateAPI:
    """Futures funding rate endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Funding Rate API with client."""
        self.client = client
    
    def get_history(self, symbol: str, interval: str) -> List[Dict[str, Any]]:
        """
        Get funding rate history in OHLC format.
        
        Args:
            symbol: Futures instrument identifier (e.g., 'BTCUSDT_PERP')
            interval: Interval for funding rate data
        
        Returns:
            List of funding rate OHLC data
        """
        params = {
            'symbol': symbol,
            'interval': interval
        }
        response = self.client.get('/futures/funding-rate/history', params=params)
        return response.get('data', [])
    
    def get_oi_weight_history(self, symbol: str, interval: str) -> List[Dict[str, Any]]:
        """
        Get open interest-weighted average funding rate history.
        
        Args:
            symbol: Cryptocurrency symbol (e.g., 'BTC')
            interval: Interval for funding rate data
        
        Returns:
            List of OI-weighted funding rate data
        """
        params = {
            'symbol': symbol,
            'interval': interval
        }
        response = self.client.get('/futures/funding-rate/oi-weight-history', params=params)
        return response.get('data', [])
    
    def get_vol_weight_history(self, symbol: str, interval: str) -> List[Dict[str, Any]]:
        """
        Get volume-weighted average funding rate history.
        
        Args:
            symbol: Cryptocurrency symbol (e.g., 'BTC')
            interval: Interval for funding rate data
        
        Returns:
            List of volume-weighted funding rate data
        """
        params = {
            'symbol': symbol,
            'interval': interval
        }
        response = self.client.get('/futures/funding-rate/vol-weight-history', params=params)
        return response.get('data', [])
    
    def get_exchange_list(self, symbol: str) -> List[Dict[str, Any]]:
        """
        Get current funding rates on each exchange for a coin.
        
        Args:
            symbol: Cryptocurrency symbol (e.g., 'BTC')
        
        Returns:
            List of funding rates by exchange
        """
        params = {'symbol': symbol}
        response = self.client.get('/futures/funding-rate/exchange-list', params=params)
        return response.get('data', [])
    
    def get_accumulated_exchange_list(self, symbol: str) -> List[Dict[str, Any]]:
        """
        Get cumulative funding rate for each exchange.
        
        Args:
            symbol: Cryptocurrency symbol (e.g., 'BTC')
        
        Returns:
            List of cumulative funding rates by exchange
        """
        params = {'symbol': symbol}
        response = self.client.get('/futures/funding-rate/accumulated-exchange-list', params=params)
        return response.get('data', [])
    
    def get_arbitrage(self, symbol: str) -> List[Dict[str, Any]]:
        """
        Get funding rate arbitrage data between exchanges.
        
        Args:
            symbol: Cryptocurrency symbol (e.g., 'BTC')
        
        Returns:
            List of arbitrage opportunities
        """
        params = {'symbol': symbol}
        response = self.client.get('/futures/funding-rate/arbitrage', params=params)
        return response.get('data', [])