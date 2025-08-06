"""
Ethereum API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ..client import CoinGlassClient


class EthereumAPI:
    """Ethereum API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Ethereum API with client."""
        self.client = client

    def get_list(self) -> List[Dict[str, Any]]:
        """
        Get list.
        
        Returns:
            List of data
        """
        response = self.client.get('/etf/ethereum/list')
        return response.get('data', [])
    def get_flow_history(self) -> List[Dict[str, Any]]:
        """
        Get flow history.
        
        Returns:
            List of data
        """
        response = self.client.get('/etf/ethereum/flow-history')
        return response.get('data', [])