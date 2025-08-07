"""
Index API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ..client import CoinGlassClient
from ..constants import PlanLevel


class IndexAPI:
    """Index API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Index API with client."""
        self.client = client

    def get_fear_greed_history(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get historical Fear & Greed Index data.
        
        Min Plan Level: 1
        Cache: Daily update
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of fear & greed index historical data
        """
        params = {}
        # Add optional params from kwargs
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/index/fear-greed-history', params=params if params else None)
        return response.get('data', [])
    def get_option_vs_futures_oi_ratio(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get option vs futures open interest ratio.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of option vs futures OI ratio data
        """
        params = {}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/index/option-vs-futures-oi-ratio', params=params if params else None)
        return response.get('data', [])
    def get_bitcoin_vs_global_m2_growth(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get Bitcoin vs Global M2 money supply growth comparison.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of Bitcoin vs Global M2 growth data
        """
        params = {}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/index/bitcoin-vs-global-m2-growth', params=params if params else None)
        return response.get('data', [])
    def get_bitcoin_vs_us_m2_growth(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get Bitcoin vs US M2 money supply growth comparison.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of Bitcoin vs US M2 growth data
        """
        params = {}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/index/bitcoin-vs-us-m2-growth', params=params if params else None)
        return response.get('data', [])
    def get_ahr999(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get AHR999 index (Bitcoin investment timing indicator).
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of AHR999 index data
        """
        params = {}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/index/ahr999', params=params if params else None)
        return response.get('data', [])
    def get_two_year_ma_multiplier(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get 2-Year MA Multiplier indicator.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of 2-Year MA Multiplier data
        """
        params = {}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/index/2-year-ma-multiplier', params=params if params else None)
        return response.get('data', [])
    def get_two_hundred_week_moving_avg_heatmap(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get 200-Week Moving Average Heatmap.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of 200-Week MA Heatmap data
        """
        params = {}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/index/200-week-moving-average-heatmap', params=params if params else None)
        return response.get('data', [])
    def get_altcoin_season_index(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get Altcoin Season Index.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of Altcoin Season Index data
        """
        params = {}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/index/altcoin-season', params=params if params else None)
        return response.get('data', [])
    def get_bitcoin_short_term_holder_sopr(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get Bitcoin Short-Term Holder SOPR (Spent Output Profit Ratio).
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of Bitcoin STH SOPR data
        """
        params = {}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/index/bitcoin-sth-sopr', params=params if params else None)
        return response.get('data', [])
    def get_bitcoin_long_term_holder_sopr(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get Bitcoin Long-Term Holder SOPR (Spent Output Profit Ratio).
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of Bitcoin LTH SOPR data
        """
        params = {}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/index/bitcoin-lth-sopr', params=params if params else None)
        return response.get('data', [])
    def get_bitcoin_short_term_holder_realized_price(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get Bitcoin Short-Term Holder Realized Price.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of Bitcoin STH Realized Price data
        """
        params = {}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/index/bitcoin-sth-realized-price', params=params if params else None)
        return response.get('data', [])
    def get_bitcoin_long_term_holder_realized_price(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get Bitcoin Long-Term Holder Realized Price.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of Bitcoin LTH Realized Price data
        """
        params = {}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/index/bitcoin-lth-realized-price', params=params if params else None)
        return response.get('data', [])
    def get_bitcoin_short_term_holder_supply(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get Bitcoin Short-Term Holder Supply.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of Bitcoin STH Supply data
        """
        params = {}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/index/bitcoin-short-term-holder-supply', params=params if params else None)
        return response.get('data', [])
    def get_bitcoin_long_term_holder_supply(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get Bitcoin Long-Term Holder Supply.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of Bitcoin LTH Supply data
        """
        params = {}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/index/bitcoin-long-term-holder-supply', params=params if params else None)
        return response.get('data', [])
    def get_bitcoin_rhodl_ratio(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get Bitcoin RHODL Ratio (Realized HODL Ratio).
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of Bitcoin RHODL Ratio data
        """
        params = {}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/index/bitcoin-rhodl-ratio', params=params if params else None)
        return response.get('data', [])
    def get_bitcoin_reserve_risk(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get Bitcoin Reserve Risk indicator.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of Bitcoin Reserve Risk data
        """
        params = {}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/index/bitcoin-reserve-risk', params=params if params else None)
        return response.get('data', [])
    def get_bitcoin_active_addresses(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get Bitcoin Active Addresses count.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of Bitcoin Active Addresses data
        """
        params = {}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/index/bitcoin-active-addresses', params=params if params else None)
        return response.get('data', [])
    def get_bitcoin_new_addresses(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get Bitcoin New Addresses count.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of Bitcoin New Addresses data
        """
        params = {}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/index/bitcoin-new-addresses', params=params if params else None)
        return response.get('data', [])
    def get_bitcoin_net_unrealized_pnl(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get Bitcoin Net Unrealized Profit/Loss (NUPL).
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of Bitcoin NUPL data
        """
        params = {}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/index/bitcoin-net-unrealized-profit-loss', params=params if params else None)
        return response.get('data', [])
    def get_btc_correlations(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        # period: int = None - Correlation period in days
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get Bitcoin correlations with other assets.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
                - period (int): Correlation period in days
        
        Returns:
            List of Bitcoin correlation data
        """
        params = {}
        for key in ['startTime', 'endTime', 'period']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/index/bitcoin-correlation', params=params if params else None)
        return response.get('data', [])
    def get_bitcoin_macro_oscillator(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get Bitcoin Macro Oscillator indicator.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of Bitcoin Macro Oscillator data
        """
        params = {}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/index/bitcoin-macro-oscillator', params=params if params else None)
        return response.get('data', [])