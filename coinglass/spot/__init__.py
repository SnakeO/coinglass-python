"""
Spot API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ..client import CoinGlassClient


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
        Get supported coins.
        
        Returns:
            List of data
        """
        response = self.client.get('/spot/supported-coins')
        return response.get('data', [])
    def get_supported_exchange_pairs(self) -> List[Dict[str, Any]]:
        """
        Get supported exchange pairs.
        
        Returns:
            List of data
        """
        response = self.client.get('/spot/supported-exchange-pairs')
        return response.get('data', [])
    def get_coins_markets(self) -> List[Dict[str, Any]]:
        """
        Get coins markets.
        
        Returns:
            List of data
        """
        response = self.client.get('/spot/coins-markets')
        return response.get('data', [])
    def get_pairs_markets(self) -> List[Dict[str, Any]]:
        """
        Get pairs markets.
        
        Returns:
            List of data
        """
        response = self.client.get('/spot/pairs-markets')
        return response.get('data', [])