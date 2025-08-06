"""
Tx API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ...client import CoinGlassClient


class TxAPI:
    """Tx API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Tx API with client."""
        self.client = client

    def get_list(self, exchange: str, symbol: Optional[str]= None) -> List[Dict[str, Any]]:
        """
        Get list.
        
        Args:
            exchange: Exchange
            symbol: Symbol (optional)
        
        Returns:
            List of data
        """
        params = {
            'exchange': exchange,
            'symbol': symbol,
        }
        params = {k: v for k, v in params.items() if v is not None}
        response = self.client.get('/exchange/chain/tx/list', params=params)
        return response.get('data', [])