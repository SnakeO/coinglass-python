"""
NetAssets API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ....client import CoinGlassClient
from ....constants import PlanLevel


class NetAssetsAPI:
    """NetAssets API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize NetAssets API with client."""
        self.client = client

    def get_history(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get Bitcoin ETF net assets history.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of Bitcoin ETF net assets historical data
        """
        params = {}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/etf/bitcoin/net-assets/history', params=params if params else None)
        return response.get('data', [])