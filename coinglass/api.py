"""
Main CoinGlass API interface
Aggregates all API modules for easy access
"""
from typing import Optional, List, Dict, Any
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
from .endpoints import EndpointRegistry

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
        session: Optional[requests.Session] = None,
        plan_level: Optional[int] = None
    ):
        """
        Initialize CoinGlass API interface.
        
        Args:
            api_key: Your CoinGlass API key. If not provided, will look for CG_API_KEY env var.
            base_url: Override the default API base URL
            timeout: Request timeout in seconds
            max_retries: Maximum number of retry attempts for failed requests
            session: Optional requests.Session to use for HTTP requests
            plan_level: Your API plan level (1-5). If not provided, will look for PLAN_LEVEL env var.
        """
        # Initialize base client
        self.client = CoinGlassClient(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            session=session
        )
        
        # Store plan level (default to 1 if not specified)
        import os
        self.plan_level = plan_level or int(os.getenv('PLAN_LEVEL', '1'))
        
        # Initialize endpoint registry
        self.endpoint_registry = EndpointRegistry()
        
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
    def get_coinbase_premium_index(self, interval: Optional[str] = None, **kwargs):
        """
        Get Coinbase Premium Index data.
        
        Min Plan Level: 1
        
        Args:
            interval: Time interval (e.g., '1h', '4h', '1d') - optional
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        """
        return coinbase_premium_index.get_coinbase_premium_index(self.client, interval, **kwargs)
    
    def get_bitfinex_margin_long_short(self, **kwargs):
        """
        Get Bitfinex margin long vs short positions data.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        """
        return bitfinex_margin_long_short.get_bitfinex_margin_long_short(self.client, **kwargs)
    
    def get_borrow_interest_rate_history(self, **kwargs):
        """
        Get historical borrow interest rate data.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        """
        return borrow_interest_rate.history.get_history(self.client, **kwargs)
    
    def get_ahr999(self, **kwargs):
        """
        Get AHR999 indicator data.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        """
        return ahr999.get_ahr999(self.client, **kwargs)
    
    def get_bull_market_peak_indicator(self, **kwargs):
        """
        Get bull market peak indicators.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        """
        return bull_market_peak_indicator.get_bull_market_peak_indicator(self.client, **kwargs)
    
    def get_puell_multiple(self, **kwargs):
        """
        Get Puell Multiple data.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        """
        return puell_multiple.get_puell_multiple(self.client, **kwargs)
    
    def get_stock_to_flow(self, **kwargs):
        """
        Get Stock-to-Flow model data.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        """
        return stock_to_flow.get_stock_to_flow(self.client, **kwargs)
    
    def get_pi_cycle_top_indicator(self, **kwargs):
        """
        Get Pi Cycle Top Indicator data.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        """
        return pi_cycle_top_indicator.get_pi_cycle_top_indicator(self.client, **kwargs)
    
    def get_golden_ratio_multiplier(self, **kwargs):
        """
        Get Golden Ratio Multiplier data.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        """
        return golden_ratio_multiplier.get_golden_ratio_multiplier(self.client, **kwargs)
    
    def get_bitcoin_profitable_days(self, **kwargs):
        """
        Get percentage of profitable days in Bitcoin history.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        """
        return bitcoin_profitable_days.get_bitcoin_profitable_days(self.client, **kwargs)
    
    def get_bitcoin_rainbow_chart(self, **kwargs):
        """
        Get Bitcoin Rainbow Chart data.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        """
        return bitcoin_rainbow_chart.get_bitcoin_rainbow_chart(self.client, **kwargs)
    
    # Utility methods for endpoint access management
    def get_available_endpoints(self, plan_level: Optional[int] = None) -> List[str]:
        """
        Get list of endpoints available for the current or specified plan level.
        
        Args:
            plan_level: Optional plan level to check (1-5). Uses instance plan_level if not provided.
            
        Returns:
            List of endpoint names available for the plan level
        """
        level = plan_level or self.plan_level
        return self.endpoint_registry.get_available_endpoints(level)
    
    def check_endpoint_access(self, endpoint_name: str, plan_level: Optional[int] = None) -> bool:
        """
        Check if an endpoint is accessible with the current or specified plan level.
        
        Args:
            endpoint_name: Name of the endpoint to check
            plan_level: Optional plan level to check (1-5). Uses instance plan_level if not provided.
            
        Returns:
            True if endpoint is accessible, False otherwise
        """
        level = plan_level or self.plan_level
        return self.endpoint_registry.check_endpoint_access(endpoint_name, level)
    
    def get_plan_level(self) -> int:
        """
        Get the current plan level.
        
        Returns:
            Current plan level (1-5)
        """
        return self.plan_level
    
    def get_plan_name(self) -> str:
        """
        Get the name of the current plan level.
        
        Returns:
            Plan name (e.g., 'Hobbyist', 'Professional')
        """
        from .constants import PlanLevel
        return PlanLevel.get_name(self.plan_level)
    
    def get_endpoint_statistics(self) -> Dict[str, any]:
        """
        Get statistics about endpoint availability for current plan.
        
        Returns:
            Dictionary with statistics including total available endpoints
        """
        stats = self.endpoint_registry.get_statistics()
        stats['current_plan_level'] = self.plan_level
        stats['current_plan_name'] = self.get_plan_name()
        stats['available_endpoints_count'] = len(self.get_available_endpoints())
        return stats
    
    def close(self):
        """Close the underlying session."""
        self.client.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()