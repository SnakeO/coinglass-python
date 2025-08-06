"""
Bitcoin Rainbow Chart endpoint
"""
from typing import Optional, Dict, Any
from .client import CoinGlassClient


def get_bitcoin_rainbow_chart(client: CoinGlassClient) -> Dict[str, Any]:
    """
    Get bitcoin rainbow chart.
    
    Args:
        client: CoinGlass API client

    
    Returns:
        Data dictionary
    """
    response = client.get('/bitcoin-rainbow-chart')
    return response.get('data', {})