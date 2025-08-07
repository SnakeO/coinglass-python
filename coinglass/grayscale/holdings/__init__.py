"""
Holdings API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ...client import CoinGlassClient
from ...constants import PlanTier


class HoldingsAPI:
    """Holdings API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Holdings API with client."""
        self.client = client

    def get_list(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get Grayscale holdings list.
        
        Plan Availability: All plans
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of Grayscale holdings data
        """
        params = {}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/grayscale/holdings-list', params=params if params else None)
        return response.get('data', [])