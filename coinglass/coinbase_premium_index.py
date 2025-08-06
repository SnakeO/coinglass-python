"""
Coinbase Premium Index endpoint
"""
from typing import Optional, Dict, Any
from .client import CoinGlassClient


def get_coinbase_premium_index(client: CoinGlassClient, interval: Optional[str]= None) -> Dict[str, Any]:
    """
    Get coinbase premium index.
    
    Args:
        client: CoinGlass API client

        interval: Interval (optional)
    
    Returns:
        Data dictionary
    """
    params = {
        'interval': interval,
    }
    params = {k: v for k, v in params.items() if v is not None}
    response = client.get('/coinbase-premium-index', params=params)
    return response.get('data', {})