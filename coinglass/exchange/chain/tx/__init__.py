"""
Tx API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ....client import CoinGlassClient
from ....constants import PlanLevel


class TxAPI:
    """Tx API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Tx API with client."""
        self.client = client

    def get_list(
        self,
        exchange: str,
        symbol: Optional[str] = None,
        # Optional parameters (can be passed as kwargs):
        # chain: str = None - Specific blockchain network
        # txType: str = None - Transaction type (deposit/withdrawal)
        # limit: int = None - Number of results to return
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get on-chain transaction list for an exchange.
        
        Min Plan Level: 1
        
        Args:
            exchange: Exchange name (e.g., 'Binance', 'Coinbase')
            symbol: Symbol (e.g., 'BTC', 'ETH') - optional
            **kwargs: Optional parameters:
                - chain (str): Specific blockchain network
                - txType (str): Transaction type (deposit/withdrawal)
                - limit (int): Number of results to return
        
        Returns:
            List of on-chain transaction data
        """
        params = {
            'ex': exchange,
        }
        if symbol is not None:
            params['symbol'] = symbol
        
        # Add optional params from kwargs
        for key in ['chain', 'txType', 'limit']:
            if key in kwargs:
                params[key] = kwargs[key]
        response = self.client.get('/exchange/chain/tx/list', params=params)
        return response.get('data', [])