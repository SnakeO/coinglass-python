"""
Option API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from .client import CoinGlassClient


class OptionAPI:
    """Option API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Option API with client."""
        self.client = client

    def get_max_pain(self, symbol: str) -> List[Dict[str, Any]]:
        """
        Get max pain.
        
        Args:
            symbol: Symbol
        
        Returns:
            List of data
        """
        params = {
            'symbol': symbol,
        }
        response = self.client.get('/option/max-pain', params=params)
        return response.get('data', [])
    def get_info(self, symbol: str) -> Dict[Dict[str, Any]]:
        """
        Get info.
        
        Args:
            symbol: Symbol
        
        Returns:
            Data dictionary
        """
        params = {
            'symbol': symbol,
        }
        response = self.client.get('/option/info', params=params)
        return response.get('data', {})
    def get_exchange_oi_history(self, symbol: str, unit: Optional[str]= None, range: Optional[str]= None) -> List[Dict[str, Any]]:
        """
        Get exchange oi history.
        
        Args:
            symbol: Symbol
            unit: Unit (optional)
            range: Range (optional)
        
        Returns:
            List of data
        """
        params = {
            'symbol': symbol,
            'unit': unit,
            'range': range,
        }
        params = {k: v for k, v in params.items() if v is not None}
        response = self.client.get('/option/exchange-oi-history', params=params)
        return response.get('data', [])
    def get_exchange_vol_history(self, symbol: str, unit: Optional[str]= None, range: Optional[str]= None) -> List[Dict[str, Any]]:
        """
        Get exchange vol history.
        
        Args:
            symbol: Symbol
            unit: Unit (optional)
            range: Range (optional)
        
        Returns:
            List of data
        """
        params = {
            'symbol': symbol,
            'unit': unit,
            'range': range,
        }
        params = {k: v for k, v in params.items() if v is not None}
        response = self.client.get('/option/exchange-vol-history', params=params)
        return response.get('data', [])