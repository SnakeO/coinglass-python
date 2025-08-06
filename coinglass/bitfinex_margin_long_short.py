"""
Bitfinex Margin Long Short endpoint
"""
from typing import Optional, Dict, Any
from .client import CoinGlassClient


def get_bitfinex_margin_long_short(client: CoinGlassClient) -> Dict[str, Any]:
    """
    Get bitfinex margin long short.
    
    Args:
        client: CoinGlass API client

    
    Returns:
        Data dictionary
    """
    response = client.get('/bitfinex-margin-long-short')
    return response.get('data', {})