"""
Premium API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ...client import CoinGlassClient
from ...constants import PlanLevel


class PremiumAPI:
    """Premium API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Premium API with client."""
        self.client = client

    def get_history(
        self,
        symbol: Optional[str] = None,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get Grayscale premium history.
        
        Min Plan Level: 1
        
        Args:
            symbol: Symbol (e.g., 'GBTC', 'ETHE') - optional
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of Grayscale premium history data
        """
        params = {}
        if symbol is not None:
            params['symbol'] = symbol
        
        # Add optional params from kwargs
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/grayscale/premium-history', params=params if params else None)
        return response.get('data', [])