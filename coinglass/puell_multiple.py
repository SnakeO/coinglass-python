"""
Puell Multiple endpoint
"""
from typing import Optional, Dict, Any
from .client import CoinGlassClient


def get_puell_multiple(client: CoinGlassClient) -> Dict[str, Any]:
    """
    Get puell multiple.
    
    Args:
        client: CoinGlass API client

    
    Returns:
        Data dictionary
    """
    response = client.get('/index/puell-multiple')
    return response.get('data', {})