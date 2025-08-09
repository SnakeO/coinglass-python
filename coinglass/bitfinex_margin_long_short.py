"""
Bitfinex Margin Long Short endpoint
"""
from typing import Optional, Dict, Any
from .client import CoinGlassClient


def get_bitfinex_margin_long_short(
    client: CoinGlassClient,
    symbol: str,
    interval: str,
    # Optional parameters (can be passed as kwargs):
    # startTime: int = None - Start timestamp in milliseconds
    # endTime: int = None - End timestamp in milliseconds
    # limit: int = None - Number of results (max: 1000)
    **kwargs
) -> Dict[str, Any]:
    """
    Get Bitfinex margin long/short data.
    
    Args:
        client: CoinGlass API client
        symbol: Symbol (e.g., 'BTC')
        interval: Interval (e.g., '1h', '4h', '1d')
        **kwargs: Optional parameters:
            - startTime (int): Start timestamp in milliseconds
            - endTime (int): End timestamp in milliseconds
            - limit (int): Number of results (max: 1000)
    
    Returns:
        List of Bitfinex margin long/short data
    """
    params = {
        'symbol': symbol,
        'interval': interval
    }
    # Add optional params from kwargs
    for key in ['startTime', 'endTime', 'limit']:
        if key in kwargs:
            params[key] = kwargs[key]
    
    response = client.get('/bitfinex-margin-long-short', params=params)
    return response.get('data', [])