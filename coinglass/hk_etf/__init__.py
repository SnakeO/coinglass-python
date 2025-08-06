"""
Hong Kong ETF API for CoinGlass
"""
from typing import Optional, Dict, Any
from ..client import CoinGlassClient


class HKEtfAPI:
    """Hong Kong ETF API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize HK ETF API with client."""
        self.client = client
        
        # Initialize sub-modules
        from .bitcoin import BitcoinAPI
        
        self.bitcoin = BitcoinAPI(client)