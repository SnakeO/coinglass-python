"""
Golden Ratio Multiplier endpoint
"""
from typing import Optional, Dict, Any
from .client import CoinGlassClient


def get_golden_ratio_multiplier(client: CoinGlassClient) -> Dict[str, Any]:
    """
    Get golden ratio multiplier.
    
    Args:
        client: CoinGlass API client

    
    Returns:
        Data dictionary
    """
    response = client.get('/golden-ratio-multiplier')
    return response.get('data', {})