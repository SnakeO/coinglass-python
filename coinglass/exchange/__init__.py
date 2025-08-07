"""
Exchange API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ..client import CoinGlassClient
from ..constants import PlanLevel


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

    def get_assets(
        self,
        exchange: str,
        # Optional parameters (can be passed as kwargs):
        # limit: int = None - Number of results to return
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get exchange assets and balances.
        
        Min Plan Level: 1
        Cache: Every 1 hour
        
        Args:
            exchange: Exchange name (e.g., 'Binance', 'Coinbase')
            **kwargs: Optional parameters:
                - limit (int): Number of results to return
        
        Returns:
            List of exchange asset data
        """
        params = {
            'exchange': exchange,
        }
        # Add optional params from kwargs
        for key in ['limit']:
            if key in kwargs:
                params[key] = kwargs[key]
        response = self.client.get('/exchange/assets', params=params)
        return response.get('data', [])