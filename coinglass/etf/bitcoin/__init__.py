"""
Bitcoin API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ..client import CoinGlassClient


class BitcoinAPI:
    """Bitcoin API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Bitcoin API with client."""
        self.client = client

    def get_list(self) -> List[Dict[str, Any]]:
        """
        Get list.
        
        Returns:
            List of data
        """
        response = self.client.get('/etf/bitcoin/list')
        return response.get('data', [])
    def get_flow_history(self) -> List[Dict[str, Any]]:
        """
        Get flow history.
        
        Returns:
            List of data
        """
        response = self.client.get('/etf/bitcoin/flow-history')
        return response.get('data', [])
    def get_history(self) -> List[Dict[str, Any]]:
        """
        Get history.
        
        Returns:
            List of data
        """
        response = self.client.get('/etf/bitcoin/history')
        return response.get('data', [])
    def get_detail(self) -> Dict[Dict[str, Any]]:
        """
        Get detail.
        
        Returns:
            Data dictionary
        """
        response = self.client.get('/etf/bitcoin/detail')
        return response.get('data', {})
    def get_aum(self) -> Dict[Dict[str, Any]]:
        """
        Get aum.
        
        Returns:
            Data dictionary
        """
        response = self.client.get('/etf/bitcoin/aum')
        return response.get('data', {})