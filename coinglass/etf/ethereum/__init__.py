"""
Ethereum API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ...client import CoinGlassClient
from ...constants import PlanLevel


class EthereumAPI:
    """Ethereum API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Ethereum API with client."""
        self.client = client
        
        # Initialize sub-modules
        from .net_assets import NetAssetsAPI
        
        self.net_assets = NetAssetsAPI(client)

    def get_list(
        self,
        # Optional parameters (can be passed as kwargs):
        # limit: int = None - Number of results to return
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get list of Ethereum ETFs.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - limit (int): Number of results to return
        
        Returns:
            List of Ethereum ETF data
        """
        params = {}
        for key in ['limit']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/etf/ethereum/list', params=params if params else None)
        return response.get('data', [])
    def get_flow_history(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get Ethereum ETF flow history.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of Ethereum ETF flow history data
        """
        params = {}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/etf/ethereum/flow-history', params=params if params else None)
        return response.get('data', [])