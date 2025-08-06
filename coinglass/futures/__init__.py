"""
CoinGlass Futures API Module
Provides access to all futures-related endpoints
"""
from typing import Optional, Dict, Any, List
from ..client import CoinGlassClient


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
        from .orderbook import OrderBookAPI
        from .taker_buy_sell_volume import TakerBuySellVolumeAPI
        from .aggregated_taker_buy_sell_volume import AggregatedTakerBuySellVolumeAPI
        from .global_long_short_account_ratio import GlobalLongShortAccountRatioAPI
        from .top_long_short_account_ratio import TopLongShortAccountRatioAPI
        from .top_long_short_position_ratio import TopLongShortPositionRatioAPI
        from .rsi import RSIAPI
        
        self.price = PriceAPI(client)
        self.open_interest = OpenInterestAPI(client)
        self.funding_rate = FundingRateAPI(client)
        self.liquidation = LiquidationAPI(client)
        self.orderbook = OrderBookAPI(client)
        self.taker_buy_sell_volume = TakerBuySellVolumeAPI(client)
        self.aggregated_taker_buy_sell_volume = AggregatedTakerBuySellVolumeAPI(client)
        self.global_long_short_account_ratio = GlobalLongShortAccountRatioAPI(client)
        self.top_long_short_account_ratio = TopLongShortAccountRatioAPI(client)
        self.top_long_short_position_ratio = TopLongShortPositionRatioAPI(client)
        self.rsi = RSIAPI(client)
    
    # Direct endpoint methods
    def get_supported_coins(self) -> List[str]:
        """
        Get all supported futures coins on CoinGlass.
        
        Returns:
            List of supported coin symbols
        """
        response = self.client.get('/futures/supported-coins')
        return response.get('data', [])
    
    def get_supported_exchange_pairs(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Get all supported futures trading exchanges and their trading pairs.
        
        Returns:
            Dictionary mapping exchange names to their trading pairs
        """
        response = self.client.get('/futures/supported-exchange-pairs')
        return response.get('data', {})
    
    def get_coins_markets(self) -> List[Dict[str, Any]]:
        """
        Get performance metrics for all futures coins.
        
        Returns:
            List of coin market data
        """
        response = self.client.get('/futures/coins-markets')
        return response.get('data', [])
    
    def get_pairs_markets(self) -> List[Dict[str, Any]]:
        """
        Get performance metrics for all futures trading pairs.
        
        Returns:
            List of pair market data
        """
        response = self.client.get('/futures/pairs-markets')
        return response.get('data', [])
    
    def get_coins_price_change(self) -> List[Dict[str, Any]]:
        """
        Get percentage price changes and price amplitude for all supported coins.
        
        Returns:
            List of coin price change data
        """
        response = self.client.get('/futures/coins-price-change')
        return response.get('data', [])
    
    def get_delisted_pairs(self) -> List[str]:
        """
        Get list of delisted futures trading pairs.
        
        Returns:
            List of delisted pair identifiers
        """
        response = self.client.get('/futures/delisted-pairs')
        return response.get('data', [])
    
    def get_exchange_rank(self) -> List[Dict[str, Any]]:
        """
        Get ranking of futures exchanges.
        
        Returns:
            List of exchange ranking data
        """
        response = self.client.get('/futures/exchange-rank')
        return response.get('data', [])
    
    def get_basis(self, symbol: Optional[str] = None) -> Dict[str, Any]:
        """
        Get futures basis data.
        
        Args:
            symbol: Cryptocurrency symbol (optional)
        
        Returns:
            Basis data
        """
        params = {'symbol': symbol} if symbol else {}
        response = self.client.get('/futures/basis', params=params)
        return response.get('data', {})
    
    def get_whale_index(self) -> Dict[str, Any]:
        """
        Get Whale Index data.
        
        Returns:
            Whale index data
        """
        response = self.client.get('/futures/whale-index')
        return response.get('data', {})
    
    def get_cgdi_index(self) -> Dict[str, Any]:
        """
        Get CoinGlass Derivatives Index (CGDI).
        
        Returns:
            CGDI data
        """
        response = self.client.get('/futures/cgdi-index')
        return response.get('data', {})
    
    def get_cdri_index(self) -> Dict[str, Any]:
        """
        Get CoinGlass Derivatives Risk Index (CDRI).
        
        Returns:
            CDRI data
        """
        response = self.client.get('/futures/cdri-index')
        return response.get('data', {})