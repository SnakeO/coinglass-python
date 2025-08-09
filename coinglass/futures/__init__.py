"""
CoinGlass Futures API Module
Provides access to all futures-related endpoints
"""
from typing import Optional, Dict, Any, List
from ..client import CoinGlassClient
from ..constants import PlanLevel, CacheTime


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
        
        Min Plan Level: 1
        
        Returns:
            List of supported coin symbols
        """
        response = self.client.get('/futures/supported-coins')
        return response.get('data', [])
    
    def get_supported_exchange_pairs(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Get all supported futures trading exchanges and their trading pairs.
        
        Min Plan Level: 1
        
        Returns:
            Dictionary mapping exchange names to their trading pairs
        """
        response = self.client.get('/futures/supported-exchange-pairs')
        return response.get('data', {})
    
    def get_coins_markets(self) -> List[Dict[str, Any]]:
        """
        Get performance metrics for all futures coins.
        
        Min Plan Level: 3
        
        Returns:
            List of coin market data
        """
        response = self.client.get('/futures/coins-markets')
        return response.get('data', [])
    
    def get_pairs_markets(self, symbol: str) -> List[Dict[str, Any]]:
        """
        Get performance metrics for futures trading pairs.
        
        Min Plan Level: 1
        
        Args:
            symbol: Cryptocurrency symbol (e.g., 'BTC')
        
        Returns:
            List of pair market data
        """
        params = {'symbol': symbol}
        response = self.client.get('/futures/pairs-markets', params=params)
        return response.get('data', [])
    
    def get_coins_price_change(self) -> List[Dict[str, Any]]:
        """
        Get percentage price changes and price amplitude for all supported coins.
        
        Min Plan Level: 1
        
        Returns:
            List of coin price change data
        """
        response = self.client.get('/futures/coins-price-change')
        return response.get('data', [])
    
    def get_delisted_pairs(self) -> List[str]:
        """
        Get list of delisted futures trading pairs.
        
        Min Plan Level: 1
        
        Returns:
            List of delisted pair identifiers
        """
        response = self.client.get('/futures/delisted-exchange-pairs')
        return response.get('data', [])
    
    def get_exchange_rank(self) -> List[Dict[str, Any]]:
        """
        Get ranking of futures exchanges.
        
        Min Plan Level: 1
        
        Returns:
            List of exchange ranking data
        """
        response = self.client.get('/futures/exchange-rank')
        return response.get('data', [])
    
    def get_basis(
        self, 
        exchange: str,
        symbol: str,
        interval: str,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        # limit: int = None - Number of results (max: 1000)
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get futures basis history data.
        
        Min Plan Level: 1
        
        Args:
            exchange: Exchange name (e.g., 'Binance')
            symbol: Symbol (e.g., 'BTCUSDT')
            interval: Interval (1m, 3m, 5m, 15m, 30m, 1h, 4h, 6h, 8h, 12h, 1d, 1w)
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
                - limit (int): Number of results (max: 1000)
        
        Returns:
            List of basis history data
        """
        params = {
            'exchange': exchange,
            'symbol': symbol,
            'interval': interval
        }
        # Add optional params from kwargs
        for key in ['startTime', 'endTime', 'limit']:
            if key in kwargs:
                params[key] = kwargs[key]
        response = self.client.get('/futures/basis/history', params=params)
        return response.get('data', [])
    
    def get_whale_index(
        self,
        exchange: str,
        symbol: str,
        interval: str,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        # limit: int = None - Number of results (max: 1000)
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get Whale Index history data.
        
        Min Plan Level: 2
        
        Args:
            exchange: Exchange name (e.g., 'Binance')
            symbol: Symbol (e.g., 'BTCUSDT')
            interval: Interval (1m, 3m, 5m, 15m, 30m, 1h, 4h, 6h, 8h, 12h, 1d, 1w)
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
                - limit (int): Number of results (max: 1000)
        
        Returns:
            List of whale index history data
        """
        params = {
            'exchange': exchange,
            'symbol': symbol,
            'interval': interval
        }
        # Add optional params from kwargs
        for key in ['startTime', 'endTime', 'limit']:
            if key in kwargs:
                params[key] = kwargs[key]
        response = self.client.get('/futures/whale-index/history', params=params)
        return response.get('data', [])
    
    def get_cgdi_index(self) -> Dict[str, Any]:
        """
        Get CoinGlass Derivatives Index (CGDI).
        
        Min Plan Level: 1
        Cache: Real-time
        
        Returns:
            CGDI data
        """
        response = self.client.get('/futures/cgdi-index/history')
        return response.get('data', {})
    
    def get_cdri_index(self) -> Dict[str, Any]:
        """
        Get CoinGlass Derivatives Risk Index (CDRI).
        
        Min Plan Level: 1
        Cache: Real-time
        
        Returns:
            CDRI data
        """
        response = self.client.get('/futures/cdri-index/history')
        return response.get('data', {})