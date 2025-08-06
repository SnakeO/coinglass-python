"""
Pi Cycle Top Indicator endpoint
"""
from typing import Optional, Dict, Any
from .client import CoinGlassClient


def get_pi_cycle_top_indicator(client: CoinGlassClient) -> Dict[str, Any]:
    """
    Get pi cycle top indicator.
    
    Args:
        client: CoinGlass API client

    
    Returns:
        Data dictionary
    """
    response = client.get('/pi-cycle-top-indicator')
    return response.get('data', {})