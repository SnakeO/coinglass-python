"""
CoinGlass API Python Client Library

A comprehensive Python library for interacting with the CoinGlass API v4.
Provides access to futures, spot, options, on-chain data, and various market indicators.
"""

__version__ = "1.0.0"
__author__ = "CoinGlass Python"
__license__ = "MIT"

from .client import CoinGlassClient
from .exceptions import (
    CoinGlassException,
    CoinGlassAPIError,
    CoinGlassAuthenticationError,
    CoinGlassRateLimitError,
    CoinGlassValidationError,
    CoinGlassNetworkError,
    CoinGlassTimeoutError
)

# Main API class that aggregates all modules
from .api import CoinGlass

__all__ = [
    'CoinGlass',
    'CoinGlassClient',
    'CoinGlassException',
    'CoinGlassAPIError',
    'CoinGlassAuthenticationError',
    'CoinGlassRateLimitError',
    'CoinGlassValidationError',
    'CoinGlassNetworkError',
    'CoinGlassTimeoutError',
]