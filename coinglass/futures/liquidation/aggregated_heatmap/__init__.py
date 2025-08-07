"""
Aggregated Liquidation Heatmap API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ....client import CoinGlassClient
from ....constants import PlanTier


class AggregatedHeatmapAPI:
    """Aggregated Liquidation Heatmap API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Aggregated Heatmap API with client."""
        self.client = client

    def get_model1(
        self,
        symbol: str
    ) -> Dict[str, Any]:
        """
        Get aggregated liquidation heatmap across exchanges (Model 1).
        
        Plan Availability: Professional+
        
        Args:
            symbol: Symbol (e.g., 'BTC')
        
        Returns:
            Aggregated heatmap model 1 data
        """
        params = {
            'symbol': symbol,
        }
        response = self.client.get('/futures/liquidation/aggregated-heatmap/model1', params=params)
        return response.get('data', {})
    
    def get_model2(
        self,
        symbol: str
    ) -> Dict[str, Any]:
        """
        Get alternative aggregated liquidation heatmap (Model 2).
        
        Plan Availability: Professional+
        
        Args:
            symbol: Symbol (e.g., 'BTC')
        
        Returns:
            Aggregated heatmap model 2 data
        """
        params = {
            'symbol': symbol,
        }
        response = self.client.get('/futures/liquidation/aggregated-heatmap/model2', params=params)
        return response.get('data', {})
    
    def get_model3(
        self,
        symbol: str
    ) -> Dict[str, Any]:
        """
        Get third aggregated liquidation heatmap model (Model 3).
        
        Plan Availability: Professional+
        
        Args:
            symbol: Symbol (e.g., 'BTC')
        
        Returns:
            Aggregated heatmap model 3 data
        """
        params = {
            'symbol': symbol,
        }
        response = self.client.get('/futures/liquidation/aggregated-heatmap/model3', params=params)
        return response.get('data', {})