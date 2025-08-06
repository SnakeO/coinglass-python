"""
Exchange API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ..client import CoinGlassClient


class ExchangeAPI:
    """Exchange API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Exchange API with client."""
        self.client = client
        
        # Initialize sub-modules
        from .balance import BalanceAPI
        from .chain.tx import TxAPI
        
        self.balance = BalanceAPI(client)
        self.chain = type('ChainAPI', (), {'tx': TxAPI(client)})()

    def get_assets(self, exchange: str) -> List[Dict[str, Any]]:
        """
        Get assets.
        
        Args:
            exchange: Exchange
        
        Returns:
            List of data
        """
        params = {
            'exchange': exchange,
        }
        response = self.client.get('/exchange/assets', params=params)
        return response.get('data', [])