"""
Spot API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ..client import CoinGlassClient
from ..constants import PlanTier, CacheTime


class SpotAPI:
    """Spot API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Spot API with client."""
        self.client = client
        
        # Initialize sub-modules
        from .price import PriceAPI
        from .orderbook import OrderbookAPI
        from .taker_buy_sell_volume import TakerBuySellVolumeAPI
        from .aggregated_taker_buy_sell_volume import AggregatedTakerBuySellVolumeAPI
        
        self.price = PriceAPI(client)
        self.orderbook = OrderbookAPI(client)
        self.taker_buy_sell_volume = TakerBuySellVolumeAPI(client)
        self.aggregated_taker_buy_sell_volume = AggregatedTakerBuySellVolumeAPI(client)

    def get_supported_coins(self) -> List[Dict[str, Any]]:
        """
        Get all supported spot coins.
        
        Plan Availability: All plans
        Cache: Every 1 minute
        
        Returns:
            List of supported spot coins
        """
        response = self.client.get('/spot/supported-coins')
        return response.get('data', [])
    
    def get_supported_exchange_pairs(self) -> List[Dict[str, Any]]:
        """
        Get supported spot exchanges and trading pairs.
        
        Plan Availability: All plans
        
        Returns:
            List of supported exchange pairs
        """
        response = self.client.get('/spot/supported-exchange-pairs')
        return response.get('data', [])
    
    def get_coins_markets(self) -> List[Dict[str, Any]]:
        """
        Get spot coin market performance metrics.
        
        Plan Availability: Standard+
        
        Returns:
            List of coin market data
        """
        response = self.client.get('/spot/coins-markets')
        return response.get('data', [])
    
    def get_pairs_markets(self) -> List[Dict[str, Any]]:
        """
        Get spot pairs market performance data.
        
        Plan Availability: All plans
        
        Returns:
            List of pairs market data
        """
        response = self.client.get('/spot/pairs-markets')
        return response.get('data', [])