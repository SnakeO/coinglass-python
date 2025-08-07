"""
Liquidation Heatmap API for CoinGlass
"""
from typing import Optional, List, Dict, Any
from ....client import CoinGlassClient
from ....constants import PlanLevel


class HeatmapAPI:
    """Liquidation Heatmap API endpoints."""
    
    def __init__(self, client: CoinGlassClient):
        """Initialize Heatmap API with client."""
        self.client = client

    def get_model1(
        self,
        ex: str,
        symbol: str
    ) -> Dict[str, Any]:
        """
        Get liquidation heatmap visualization data (Model 1).
        
        Min Plan Level: 4
        
        Args:
            ex: Exchange name (e.g., 'Binance')
            symbol: Symbol (e.g., 'BTCUSDT')
        
        Returns:
            Heatmap model 1 data
        """
        params = {
            'ex': ex,
            'symbol': symbol,
        }
        response = self.client.get('/futures/liquidation/heatmap/model1', params=params)
        return response.get('data', {})
    
    def get_model2(
        self,
        ex: str,
        symbol: str
    ) -> Dict[str, Any]:
        """
        Get alternative liquidation heatmap model (Model 2).
        
        Min Plan Level: 4
        
        Args:
            ex: Exchange name (e.g., 'Binance')
            symbol: Symbol (e.g., 'BTCUSDT')
        
        Returns:
            Heatmap model 2 data
        """
        params = {
            'ex': ex,
            'symbol': symbol,
        }
        response = self.client.get('/futures/liquidation/heatmap/model2', params=params)
        return response.get('data', {})
    
    def get_model3(
        self,
        ex: str,
        symbol: str
    ) -> Dict[str, Any]:
        """
        Get third liquidation heatmap model (Model 3).
        
        Min Plan Level: 4
        
        Args:
            ex: Exchange name (e.g., 'Binance')
            symbol: Symbol (e.g., 'BTCUSDT')
        
        Returns:
            Heatmap model 3 data
        """
        params = {
            'ex': ex,
            'symbol': symbol,
        }
        response = self.client.get('/futures/liquidation/heatmap/model3', params=params)
        return response.get('data', {})