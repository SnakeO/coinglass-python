"""
Calendar API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ..client import CoinGlassClient
from ..constants import PlanTier, Importance


class CalendarAPI:
    """Calendar API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Calendar API with client."""
        self.client = client

    def get_economic_data(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        # importance: str = None - Event importance (low, medium, high)
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get economic calendar events and data.
        
        Plan Availability: All plans
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
                - importance (str): Event importance level (low, medium, high)
        
        Returns:
            List of economic calendar data
        """
        params = {}
        # Add optional params from kwargs
        for key in ['startTime', 'endTime', 'importance']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/calendar/economic-data', params=params if params else None)
        return response.get('data', [])