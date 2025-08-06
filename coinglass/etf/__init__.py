"""
ETF API for CoinGlass
"""
from typing import Optional, Dict, Any
from ..client import CoinGlassClient


class ETFAPI:
    """ETF API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize ETF API with client."""
        self.client = client
        
        # Initialize sub-modules
        from .bitcoin import BitcoinAPI
        from .ethereum import EthereumAPI
        
        self.bitcoin = BitcoinAPI(client)
        self.ethereum = EthereumAPI(client)