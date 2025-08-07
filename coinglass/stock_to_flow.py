"""
Stock To Flow endpoint
"""
from typing import Optional, Dict, Any
from .client import CoinGlassClient


def get_stock_to_flow(client: CoinGlassClient) -> Dict[str, Any]:
    """
    Get stock to flow.
    
    Args:
        client: CoinGlass API client

    
    Returns:
        Data dictionary
    """
    response = client.get('/index/stock-flow')
    return response.get('data', {})