"""
Ahr999 endpoint
"""
from typing import Optional, Dict, Any
from .client import CoinGlassClient
from .constants import PlanTier


def get_ahr999(
    client: CoinGlassClient,
    # Optional parameters (can be passed as kwargs):
    # startTime: int = None - Start timestamp in milliseconds
    # endTime: int = None - End timestamp in milliseconds
    **kwargs
) -> Dict[str, Any]:
    """
    Get AHR999 index (Bitcoin investment timing indicator).
    
    Plan Availability: All plans
    
    Args:
        client: CoinGlass API client
        **kwargs: Optional parameters:
            - startTime (int): Start timestamp in milliseconds
            - endTime (int): End timestamp in milliseconds
    
    Returns:
        AHR999 index data dictionary
    """
    params = {}
    for key in ['startTime', 'endTime']:
        if key in kwargs:
            params[key] = kwargs[key]
    
    response = client.get('/index/ahr999', params=params if params else None)
    return response.get('data', {})