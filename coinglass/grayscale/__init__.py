"""
Grayscale API for CoinGlass
"""
from typing import Optional, Dict, Any
from ..client import CoinGlassClient


class GrayscaleAPI:
    """Grayscale API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Grayscale API with client."""
        self.client = client
        
        # Initialize sub-modules
        from .holdings import HoldingsAPI
        from .premium import PremiumAPI
        
        self.holdings = HoldingsAPI(client)
        self.premium = PremiumAPI(client)