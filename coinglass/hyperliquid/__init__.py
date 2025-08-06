"""
Hyperliquid API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from .client import CoinGlassClient


class HyperliquidAPI:
    """Hyperliquid API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Hyperliquid API with client."""
        self.client = client

    def get_whale_alert(self) -> List[Dict[str, Any]]:
        """
        Get whale alert.
        
        Returns:
            List of data
        """
        response = self.client.get('/hyperliquid/whale-alert')
        return response.get('data', [])
    def get_whale_position(self) -> List[Dict[str, Any]]:
        """
        Get whale position.
        
        Returns:
            List of data
        """
        response = self.client.get('/hyperliquid/whale-position')
        return response.get('data', [])