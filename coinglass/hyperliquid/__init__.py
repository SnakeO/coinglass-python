"""
Hyperliquid API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ..client import CoinGlassClient
from ..constants import PlanTier, CacheTime


class HyperliquidAPI:
    """Hyperliquid API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Hyperliquid API with client."""
        self.client = client

    def get_whale_alert(self) -> List[Dict[str, Any]]:
        """
        Get real-time whale alerts on Hyperliquid (positions >$1M).
        
        Plan Availability: All plans
        Cache: Real-time
        
        Returns:
            List of whale alert data
        """
        response = self.client.get('/hyperliquid/whale-alert')
        return response.get('data', [])
    
    def get_whale_position(self) -> List[Dict[str, Any]]:
        """
        Get whale positions on Hyperliquid (>$1M notional).
        
        Plan Availability: All plans
        Cache: Real-time
        
        Returns:
            List of whale position data
        """
        response = self.client.get('/hyperliquid/whale-position')
        return response.get('data', [])