"""
Orderbook API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ..client import CoinGlassClient


class OrderbookAPI:
    """Orderbook API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Orderbook API with client."""
        self.client = client

    def get_ask_bids_history(self, symbol: str, interval: str, range: Optional[str]= None) -> List[Dict[str, Any]]:
        """
        Get ask bids history.
        
        Args:
            symbol: Symbol
            interval: Interval
            range: Range (optional)
        
        Returns:
            List of data
        """
        params = {
            'symbol': symbol,
            'interval': interval,
            'range': range,
        }
        params = {k: v for k, v in params.items() if v is not None}
        response = self.client.get('/futures/orderbook/ask-bids-history', params=params)
        return response.get('data', [])
    def get_aggregated_ask_bids_history(self, symbol: str, interval: str, range: Optional[str]= None) -> List[Dict[str, Any]]:
        """
        Get aggregated ask bids history.
        
        Args:
            symbol: Symbol
            interval: Interval
            range: Range (optional)
        
        Returns:
            List of data
        """
        params = {
            'symbol': symbol,
            'interval': interval,
            'range': range,
        }
        params = {k: v for k, v in params.items() if v is not None}
        response = self.client.get('/futures/orderbook/aggregated-ask-bids-history', params=params)
        return response.get('data', [])
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
        response = self.client.get('/futures/orderbook/history', params=params)
        return response.get('data', [])
    def get_large_limit_order(self, symbol: str) -> List[Dict[str, Any]]:
        """
        Get large limit order.
        
        Args:
            symbol: Symbol
        
        Returns:
            List of data
        """
        params = {
            'symbol': symbol,
        }
        response = self.client.get('/futures/orderbook/large-limit-order', params=params)
        return response.get('data', [])
    def get_large_limit_order_history(self, symbol: str, interval: str) -> List[Dict[str, Any]]:
        """
        Get large limit order history.
        
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
        response = self.client.get('/futures/orderbook/large-limit-order-history', params=params)
        return response.get('data', [])