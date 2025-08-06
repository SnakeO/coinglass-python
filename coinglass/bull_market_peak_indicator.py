"""
Bull Market Peak Indicator endpoint
"""
from typing import Optional, Dict, Any
from .client import CoinGlassClient


def get_bull_market_peak_indicator(client: CoinGlassClient) -> Dict[str, Any]:
    """
    Get bull market peak indicator.
    
    Args:
        client: CoinGlass API client

    
    Returns:
        Data dictionary
    """
    response = client.get('/bull-market-peak-indicator')
    return response.get('data', {})