"""
AggregatedHeatmap API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ...client import CoinGlassClient


class AggregatedHeatmapAPI:
    """AggregatedHeatmap API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize AggregatedHeatmap API with client."""
        self.client = client

    def get_model1(self, symbol: str) -> List[Dict[str, Any]]:
        """
        Get model1.
        
        Args:
            symbol: Symbol
        
        Returns:
            List of data
        """
        params = {
            'symbol': symbol,
        }
        response = self.client.get('/futures/liquidation/aggregated_heatmap/model1', params=params)
        return response.get('data', [])
    def get_model2(self, symbol: str) -> List[Dict[str, Any]]:
        """
        Get model2.
        
        Args:
            symbol: Symbol
        
        Returns:
            List of data
        """
        params = {
            'symbol': symbol,
        }
        response = self.client.get('/futures/liquidation/aggregated_heatmap/model2', params=params)
        return response.get('data', [])
    def get_model3(self, symbol: str) -> List[Dict[str, Any]]:
        """
        Get model3.
        
        Args:
            symbol: Symbol
        
        Returns:
            List of data
        """
        params = {
            'symbol': symbol,
        }
        response = self.client.get('/futures/liquidation/aggregated_heatmap/model3', params=params)
        return response.get('data', [])