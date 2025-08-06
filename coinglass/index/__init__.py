"""
Index API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from .client import CoinGlassClient


class IndexAPI:
    """Index API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Index API with client."""
        self.client = client

    def get_fear_greed_history(self) -> List[Dict[str, Any]]:
        """
        Get fear greed history.
        
        Returns:
            List of data
        """
        response = self.client.get('/index/fear-greed-history')
        return response.get('data', [])
    def get_option_vs_futures_oi_ratio(self) -> List[Dict[str, Any]]:
        """
        Get option vs futures oi ratio.
        
        Returns:
            List of data
        """
        response = self.client.get('/index/option-vs-futures-oi-ratio')
        return response.get('data', [])
    def get_bitcoin_vs_global_m2_growth(self) -> List[Dict[str, Any]]:
        """
        Get bitcoin vs global m2 growth.
        
        Returns:
            List of data
        """
        response = self.client.get('/index/bitcoin-vs-global-m2-growth')
        return response.get('data', [])
    def get_bitcoin_vs_us_m2_growth(self) -> List[Dict[str, Any]]:
        """
        Get bitcoin vs us m2 growth.
        
        Returns:
            List of data
        """
        response = self.client.get('/index/bitcoin-vs-us-m2-growth')
        return response.get('data', [])
    def get_ahr999(self) -> List[Dict[str, Any]]:
        """
        Get ahr999.
        
        Returns:
            List of data
        """
        response = self.client.get('/index/ahr999')
        return response.get('data', [])
    def get_two_year_ma_multiplier(self) -> List[Dict[str, Any]]:
        """
        Get two year ma multiplier.
        
        Returns:
            List of data
        """
        response = self.client.get('/index/2-year-ma-multiplier')
        return response.get('data', [])
    def get_two_hundred_week_moving_avg_heatmap(self) -> List[Dict[str, Any]]:
        """
        Get two hundred week moving avg heatmap.
        
        Returns:
            List of data
        """
        response = self.client.get('/index/200-week-moving-avg-heatmap')
        return response.get('data', [])
    def get_altcoin_season_index(self) -> List[Dict[str, Any]]:
        """
        Get altcoin season index.
        
        Returns:
            List of data
        """
        response = self.client.get('/index/altcoin-season-index')
        return response.get('data', [])
    def get_bitcoin_short_term_holder_sopr(self) -> List[Dict[str, Any]]:
        """
        Get bitcoin short term holder sopr.
        
        Returns:
            List of data
        """
        response = self.client.get('/index/bitcoin-short-term-holder-sopr')
        return response.get('data', [])
    def get_bitcoin_long_term_holder_sopr(self) -> List[Dict[str, Any]]:
        """
        Get bitcoin long term holder sopr.
        
        Returns:
            List of data
        """
        response = self.client.get('/index/bitcoin-long-term-holder-sopr')
        return response.get('data', [])
    def get_bitcoin_short_term_holder_realized_price(self) -> List[Dict[str, Any]]:
        """
        Get bitcoin short term holder realized price.
        
        Returns:
            List of data
        """
        response = self.client.get('/index/bitcoin-short-term-holder-realized-price')
        return response.get('data', [])
    def get_bitcoin_long_term_holder_realized_price(self) -> List[Dict[str, Any]]:
        """
        Get bitcoin long term holder realized price.
        
        Returns:
            List of data
        """
        response = self.client.get('/index/bitcoin-long-term-holder-realized-price')
        return response.get('data', [])
    def get_bitcoin_short_term_holder_supply(self) -> List[Dict[str, Any]]:
        """
        Get bitcoin short term holder supply.
        
        Returns:
            List of data
        """
        response = self.client.get('/index/bitcoin-short-term-holder-supply')
        return response.get('data', [])
    def get_bitcoin_long_term_holder_supply(self) -> List[Dict[str, Any]]:
        """
        Get bitcoin long term holder supply.
        
        Returns:
            List of data
        """
        response = self.client.get('/index/bitcoin-long-term-holder-supply')
        return response.get('data', [])
    def get_bitcoin_rhodl_ratio(self) -> List[Dict[str, Any]]:
        """
        Get bitcoin rhodl ratio.
        
        Returns:
            List of data
        """
        response = self.client.get('/index/bitcoin-rhodl-ratio')
        return response.get('data', [])
    def get_bitcoin_reserve_risk(self) -> List[Dict[str, Any]]:
        """
        Get bitcoin reserve risk.
        
        Returns:
            List of data
        """
        response = self.client.get('/index/bitcoin-reserve-risk')
        return response.get('data', [])
    def get_bitcoin_active_addresses(self) -> List[Dict[str, Any]]:
        """
        Get bitcoin active addresses.
        
        Returns:
            List of data
        """
        response = self.client.get('/index/bitcoin-active-addresses')
        return response.get('data', [])
    def get_bitcoin_new_addresses(self) -> List[Dict[str, Any]]:
        """
        Get bitcoin new addresses.
        
        Returns:
            List of data
        """
        response = self.client.get('/index/bitcoin-new-addresses')
        return response.get('data', [])
    def get_bitcoin_net_unrealized_pnl(self) -> List[Dict[str, Any]]:
        """
        Get bitcoin net unrealized pnl.
        
        Returns:
            List of data
        """
        response = self.client.get('/index/bitcoin-net-unrealized-pnl')
        return response.get('data', [])
    def get_btc_correlations(self) -> List[Dict[str, Any]]:
        """
        Get btc correlations.
        
        Returns:
            List of data
        """
        response = self.client.get('/index/btc-correlations')
        return response.get('data', [])
    def get_bitcoin_macro_oscillator(self) -> List[Dict[str, Any]]:
        """
        Get bitcoin macro oscillator.
        
        Returns:
            List of data
        """
        response = self.client.get('/index/bitcoin-macro-oscillator')
        return response.get('data', [])