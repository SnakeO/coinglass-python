"""
Main CoinGlass API interface
Aggregates all API modules for easy access
"""
from typing import Optional
import requests

from .client import CoinGlassClient
from .futures import FuturesAPI
from .spot import SpotAPI
from .option import OptionAPI
from .exchange import ExchangeAPI
from .etf import ETFAPI
from .hk_etf import HKEtfAPI
from .grayscale import GrayscaleAPI
from .index import IndexAPI
from .hyperliquid import HyperliquidAPI
from .calendar import CalendarAPI

# Import top-level indicator modules
from . import (
    coinbase_premium_index,
    bitfinex_margin_long_short,
    borrow_interest_rate,
    ahr999,
    bull_market_peak_indicator,
    puell_multiple,
    stock_to_flow,
    pi_cycle_top_indicator,
    golden_ratio_multiplier,
    bitcoin_profitable_days,
    bitcoin_rainbow_chart
)


class CoinGlass:
    """
    Main interface for the CoinGlass API.
    
    This class aggregates all API modules and provides a unified interface
    for accessing all CoinGlass API endpoints.
    
    Example:
        >>> from coinglass import CoinGlass
        >>> cg = CoinGlass(api_key="your_api_key")
        >>> 
        >>> # Access futures data
        >>> btc_markets = cg.futures.get_coins_markets()
        >>> 
        >>> # Access spot data
        >>> spot_pairs = cg.spot.get_supported_exchange_pairs()
        >>> 
        >>> # Access options data
        >>> max_pain = cg.option.get_max_pain(symbol="BTC")
        >>> 
        >>> # Access on-chain data
        >>> exchange_assets = cg.exchange.get_assets(exchange="Binance")
        >>> 
        >>> # Access indicators
        >>> fear_greed = cg.index.get_fear_greed_history()
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: int = 30,
        max_retries: int = 3,
        session: Optional[requests.Session] = None
    ):
        """
        Initialize CoinGlass API interface.
        
        Args:
            api_key: Your CoinGlass API key. If not provided, will look for CG_API_KEY env var.
            base_url: Override the default API base URL
            timeout: Request timeout in seconds
            max_retries: Maximum number of retry attempts for failed requests
            session: Optional requests.Session to use for HTTP requests
        """
        # Initialize base client
        self.client = CoinGlassClient(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            session=session
        )
        
        # Initialize API modules
        self.futures = FuturesAPI(self.client)
        self.spot = SpotAPI(self.client)
        self.option = OptionAPI(self.client)
        self.exchange = ExchangeAPI(self.client)
        self.etf = ETFAPI(self.client)
        self.hk_etf = HKEtfAPI(self.client)
        self.grayscale = GrayscaleAPI(self.client)
        self.index = IndexAPI(self.client)
        self.hyperliquid = HyperliquidAPI(self.client)
        self.calendar = CalendarAPI(self.client)
    
    # Top-level indicator methods
    def get_coinbase_premium_index(self, interval: Optional[str] = None):
        """Get Coinbase Premium Index data."""
        return coinbase_premium_index.get_coinbase_premium_index(self.client, interval)
    
    def get_bitfinex_margin_long_short(self):
        """Get Bitfinex margin long vs short positions data."""
        return bitfinex_margin_long_short.get_bitfinex_margin_long_short(self.client)
    
    def get_borrow_interest_rate_history(self):
        """Get historical borrow interest rate data."""
        return borrow_interest_rate.history.get_history(self.client)
    
    def get_ahr999(self):
        """Get AHR999 indicator data."""
        return ahr999.get_ahr999(self.client)
    
    def get_bull_market_peak_indicator(self):
        """Get bull market peak indicators."""
        return bull_market_peak_indicator.get_bull_market_peak_indicator(self.client)
    
    def get_puell_multiple(self):
        """Get Puell Multiple data."""
        return puell_multiple.get_puell_multiple(self.client)
    
    def get_stock_to_flow(self):
        """Get Stock-to-Flow model data."""
        return stock_to_flow.get_stock_to_flow(self.client)
    
    def get_pi_cycle_top_indicator(self):
        """Get Pi Cycle Top Indicator data."""
        return pi_cycle_top_indicator.get_pi_cycle_top_indicator(self.client)
    
    def get_golden_ratio_multiplier(self):
        """Get Golden Ratio Multiplier data."""
        return golden_ratio_multiplier.get_golden_ratio_multiplier(self.client)
    
    def get_bitcoin_profitable_days(self):
        """Get percentage of profitable days in Bitcoin history."""
        return bitcoin_profitable_days.get_bitcoin_profitable_days(self.client)
    
    def get_bitcoin_rainbow_chart(self):
        """Get Bitcoin Rainbow Chart data."""
        return bitcoin_rainbow_chart.get_bitcoin_rainbow_chart(self.client)
    
    def close(self):
        """Close the underlying session."""
        self.client.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()