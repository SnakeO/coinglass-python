"""
Bitcoin API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ...client import CoinGlassClient


class BitcoinAPI:
    """Bitcoin API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Bitcoin API with client."""
        self.client = client

    def get_flow_history(self) -> List[Dict[str, Any]]:
        """
        Get flow history.
        
        Returns:
            List of data
        """
        response = self.client.get('/hk-etf/bitcoin/flow-history')
        return response.get('data', [])