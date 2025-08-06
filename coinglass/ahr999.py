"""
Ahr999 endpoint
"""
from typing import Optional, Dict, Any
from .client import CoinGlassClient


def get_ahr999(client: CoinGlassClient) -> Dict[str, Any]:
    """
    Get ahr999.
    
    Args:
        client: CoinGlass API client

    
    Returns:
        Data dictionary
    """
    response = client.get('/ahr999')
    return response.get('data', {})