"""
Bitcoin Profitable Days endpoint
"""
from typing import Optional, Dict, Any
from .client import CoinGlassClient


def get_bitcoin_profitable_days(client: CoinGlassClient) -> Dict[str, Any]:
    """
    Get bitcoin profitable days.
    
    Args:
        client: CoinGlass API client

    
    Returns:
        Data dictionary
    """
    response = client.get('/index/bitcoin/profitable-days')
    return response.get('data', {})