"""
Coinbase Premium Index endpoint
"""
from typing import Optional, Dict, Any
from .client import CoinGlassClient
from .constants import PlanLevel


def get_coinbase_premium_index(
    client: CoinGlassClient,
    interval: Optional[str] = None,
    # Optional parameters (can be passed as kwargs):
    # startTime: int = None - Start timestamp in milliseconds
    # endTime: int = None - End timestamp in milliseconds
    **kwargs
) -> Dict[str, Any]:
    """
    Get Coinbase Premium Index data.
    
    Min Plan Level: 1
    
    Args:
        client: CoinGlass API client
        interval: Time interval (e.g., '1h', '4h', '1d') - optional
        **kwargs: Optional parameters:
            - startTime (int): Start timestamp in milliseconds
            - endTime (int): End timestamp in milliseconds
    
    Returns:
        Coinbase Premium Index data dictionary
    """
    params = {}
    if interval is not None:
        params['interval'] = interval
    
    # Add optional params from kwargs
    for key in ['startTime', 'endTime']:
        if key in kwargs:
            params[key] = kwargs[key]
    response = client.get('/coinbase-premium-index', params=params if params else None)
    return response.get('data', {})