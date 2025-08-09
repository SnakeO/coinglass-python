"""
Bitcoin API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ...client import CoinGlassClient
from ...constants import PlanLevel


class BitcoinAPI:
    """Bitcoin API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Bitcoin API with client."""
        self.client = client
        
        # Initialize sub-modules
        from .net_assets import NetAssetsAPI
        from .price import PriceAPI
        from .premium_discount import PremiumDiscountAPI
        
        self.net_assets = NetAssetsAPI(client)
        self.price = PriceAPI(client)
        self.premium_discount = PremiumDiscountAPI(client)

    def get_list(
        self,
        # Optional parameters (can be passed as kwargs):
        # limit: int = None - Number of results to return
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get list of Bitcoin ETFs.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - limit (int): Number of results to return
        
        Returns:
            List of Bitcoin ETF data
        """
        params = {}
        for key in ['limit']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/etf/bitcoin/list', params=params if params else None)
        return response.get('data', [])
    def get_flow_history(
        self,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get Bitcoin ETF flow history.
        
        Min Plan Level: 1
        
        Args:
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of Bitcoin ETF flow history data
        """
        params = {}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/etf/bitcoin/flow-history', params=params if params else None)
        return response.get('data', [])
    def get_history(
        self,
        ticker: str,
        # Optional parameters (can be passed as kwargs):
        # startTime: int = None - Start timestamp in milliseconds
        # endTime: int = None - End timestamp in milliseconds
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get Bitcoin ETF historical data.
        
        Min Plan Level: 1
        
        Args:
            ticker: ETF ticker symbol (e.g., 'GBTC')
            **kwargs: Optional parameters:
                - startTime (int): Start timestamp in milliseconds
                - endTime (int): End timestamp in milliseconds
        
        Returns:
            List of Bitcoin ETF historical data
        """
        params = {'ticker': ticker}
        for key in ['startTime', 'endTime']:
            if key in kwargs:
                params[key] = kwargs[key]
        
        response = self.client.get('/etf/bitcoin/history', params=params)
        return response.get('data', [])
    def get_detail(self, ticker: str) -> Dict[str, Any]:
        """
        Get Bitcoin ETF detailed information.
        
        Min Plan Level: 1
        
        Returns:
            Bitcoin ETF detailed data dictionary
        """
        params = {'ticker': ticker}
        response = self.client.get('/etf/bitcoin/detail', params=params)
        return response.get('data', {})
    def get_aum(self) -> Dict[str, Any]:
        """
        Get Bitcoin ETF Assets Under Management (AUM).
        
        Min Plan Level: 1
        
        Returns:
            Bitcoin ETF AUM data dictionary
        """
        response = self.client.get('/etf/bitcoin/aum')
        return response.get('data', {})