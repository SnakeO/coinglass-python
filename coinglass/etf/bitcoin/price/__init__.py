"""
Price API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ....client import CoinGlassClient


class PriceAPI:
    """Price API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Price API with client."""
        self.client = client

    def get_history(
        self, 
        ticker: str,
        range: str
    ) -> List[Dict[str, Any]]:
        """
        Get ETF price history.
        
        Args:
            ticker: ETF ticker symbol
            range: Time range (e.g., '1d', '7d', '30d', '90d', '1y')
        
        Returns:
            List of price history data
        """
        params = {
            'ticker': ticker,
            'range': range
        }
        response = self.client.get('/etf/bitcoin/price/history', params=params)
        return response.get('data', [])