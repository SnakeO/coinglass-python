"""
CoinGlass Futures API Module
Provides access to all futures-related endpoints
"""
from typing import Optional, Dict, Any, List
from ..client import CoinGlassClient
from ..constants import PlanTier, CacheTime


class FuturesAPI:
    """Futures API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Futures API with client."""
        self.client = client
        
        # Initialize sub-modules
        from .price import PriceAPI
        from .open_interest import OpenInterestAPI
        from .funding_rate import FundingRateAPI
        from .liquidation import LiquidationAPI
        from .orderbook import OrderbookAPI
        from .taker_buy_sell_volume import TakerBuySellVolumeAPI
        from .aggregated_taker_buy_sell_volume import AggregatedTakerBuySellVolumeAPI
        from .global_long_short_account_ratio import GlobalLongShortAccountRatioAPI
        from .top_long_short_account_ratio import TopLongShortAccountRatioAPI
        from .top_long_short_position_ratio import TopLongShortPositionRatioAPI
        from .rsi import RsiAPI
        
        self.price = PriceAPI(client)
        self.open_interest = OpenInterestAPI(client)
        self.funding_rate = FundingRateAPI(client)
        self.liquidation = LiquidationAPI(client)
        self.orderbook = OrderbookAPI(client)
        self.taker_buy_sell_volume = TakerBuySellVolumeAPI(client)
        self.aggregated_taker_buy_sell_volume = AggregatedTakerBuySellVolumeAPI(client)
        self.global_long_short_account_ratio = GlobalLongShortAccountRatioAPI(client)
        self.top_long_short_account_ratio = TopLongShortAccountRatioAPI(client)
        self.top_long_short_position_ratio = TopLongShortPositionRatioAPI(client)
        self.rsi = RsiAPI(client)
    
    # Direct endpoint methods
    def get_supported_coins(self) -> List[str]:
        """
        Get all supported futures coins on CoinGlass.
        
        Plan Availability: All plans
        
        Returns:
            List of supported coin symbols
        """
        response = self.client.get('/futures/supported-coins')
        return response.get('data', [])
    
    def get_supported_exchange_pairs(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Get all supported futures trading exchanges and their trading pairs.
        
        Plan Availability: All plans
        
        Returns:
            Dictionary mapping exchange names to their trading pairs
        """
        response = self.client.get('/futures/supported-exchange-pairs')
        return response.get('data', {})
    
    def get_coins_markets(self) -> List[Dict[str, Any]]:
        """
        Get performance metrics for all futures coins.
        
        Plan Availability: Standard+
        
        Returns:
            List of coin market data
        """
        response = self.client.get('/futures/coins-markets')
        return response.get('data', [])
    
    def get_pairs_markets(self) -> List[Dict[str, Any]]:
        """
        Get performance metrics for all futures trading pairs.
        
        Plan Availability: All plans
        
        Returns:
            List of pair market data
        """
        response = self.client.get('/futures/pairs-markets')
        return response.get('data', [])
    
    def get_coins_price_change(self) -> List[Dict[str, Any]]:
        """
        Get percentage price changes and price amplitude for all supported coins.
        
        Plan Availability: All plans
        
        Returns:
            List of coin price change data
        """
        response = self.client.get('/futures/coins-price-change')
        return response.get('data', [])
    
    def get_delisted_pairs(self) -> List[str]:
        """
        Get list of delisted futures trading pairs.
        
        Plan Availability: All plans
        
        Returns:
            List of delisted pair identifiers
        """
        response = self.client.get('/futures/delisted-exchange-pairs')
        return response.get('data', [])
    
    def get_exchange_rank(self) -> List[Dict[str, Any]]:
        """
        Get ranking of futures exchanges.
        
        Plan Availability: All plans
        
        Returns:
            List of exchange ranking data
        """
        response = self.client.get('/futures/exchange-rank')
        return response.get('data', [])
    
    def get_basis(
        self, 
        symbol: str,
        # Optional parameters (can be passed as kwargs):
        # exchange: str = None - Specific exchange name
        **kwargs
    ) -> Dict[str, Any]:
        """
        Get futures basis data.
        
        Plan Availability: All plans
        Cache: Real-time
        
        Args:
            symbol: Cryptocurrency symbol (e.g., 'BTC')
            **kwargs: Optional parameters:
                - exchange (str): Specific exchange name
        
        Returns:
            Basis data
        """
        params = {'symbol': symbol}
        if 'exchange' in kwargs:
            params['exchange'] = kwargs['exchange']
        response = self.client.get('/futures/basis/history', params=params)
        return response.get('data', {})
    
    def get_whale_index(self) -> Dict[str, Any]:
        """
        Get Whale Index data.
        
        Plan Availability: Startup+
        Cache: Every 1 minute
        
        Returns:
            Whale index data
        """
        response = self.client.get('/futures/whale-index/history')
        return response.get('data', {})
    
    def get_cgdi_index(self) -> Dict[str, Any]:
        """
        Get CoinGlass Derivatives Index (CGDI).
        
        Plan Availability: All plans
        Cache: Real-time
        
        Returns:
            CGDI data
        """
        response = self.client.get('/futures/cgdi-index/history')
        return response.get('data', {})
    
    def get_cdri_index(self) -> Dict[str, Any]:
        """
        Get CoinGlass Derivatives Risk Index (CDRI).
        
        Plan Availability: All plans
        Cache: Real-time
        
        Returns:
            CDRI data
        """
        response = self.client.get('/futures/cdri-index/history')
        return response.get('data', {})