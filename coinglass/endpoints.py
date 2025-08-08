"""
CoinGlass API Endpoints Registry
Centralized registry of all API endpoints with their plan level requirements
"""
from typing import Dict, List, Optional
from .constants import PlanLevel


class EndpointRegistry:
    """Registry of all CoinGlass API endpoints with plan level requirements."""
    
    # Complete endpoint registry with plan level requirements
    ENDPOINTS = {
        # Futures endpoints
        "futures.get_supported_coins": 1,  # All plans
        "futures.get_supported_exchange_pairs": 1,  # All plans
        "futures.get_coins_markets": 3,  # Standard+
        "futures.get_pairs_markets": 1,  # All plans
        "futures.get_coins_price_change": 3,  # Standard+ (was getting Upgrade plan error at level 2)
        "futures.get_delisted_pairs": 1,  # All plans
        "futures.get_exchange_rank": 1,  # All plans
        "futures.get_basis": 1,  # All plans
        "futures.get_whale_index": 2,  # Startup+
        "futures.get_cgdi_index": 1,  # All plans
        "futures.get_cdri_index": 1,  # All plans
        
        # Futures Price
        "futures.price.get_history": 1,  # All plans (with interval restrictions)
        
        # Futures Open Interest
        "futures.open_interest.get_history": 1,  # All plans
        "futures.open_interest.get_aggregated_history": 1,  # All plans
        "futures.open_interest.get_aggregated_stablecoin_margin_history": 1,  # All plans
        "futures.open_interest.get_aggregated_coin_margin_history": 1,  # All plans
        "futures.open_interest.get_exchange_list": 1,  # All plans
        "futures.open_interest.get_exchange_history_chart": 1,  # All plans
        
        # Futures Funding Rate
        "futures.funding_rate.get_history": 1,  # All plans
        "futures.funding_rate.get_oi_weight_history": 1,  # All plans
        "futures.funding_rate.get_vol_weight_history": 1,  # All plans
        "futures.funding_rate.get_exchange_list": 1,  # All plans
        "futures.funding_rate.get_accumulated_exchange_list": 1,  # All plans
        "futures.funding_rate.get_arbitrage": 3,  # Standard+
        
        # Futures Liquidation
        "futures.liquidation.get_history": 1,  # All plans
        "futures.liquidation.get_aggregated_history": 1,  # All plans
        "futures.liquidation.get_coin_list": 2,  # Startup+
        "futures.liquidation.get_exchange_list": 1,  # All plans
        "futures.liquidation.get_order": 3,  # Standard+
        "futures.liquidation.get_map": 4,  # Professional+
        "futures.liquidation.get_aggregated_map": 4,  # Professional+
        
        # Futures Liquidation Heatmap
        "futures.liquidation.heatmap.get_model1": 4,  # Professional+
        "futures.liquidation.heatmap.get_model2": 4,  # Professional+
        "futures.liquidation.heatmap.get_model3": 4,  # Professional+
        "futures.liquidation.aggregated_heatmap.get_model1": 4,  # Professional+
        "futures.liquidation.aggregated_heatmap.get_model2": 4,  # Professional+
        "futures.liquidation.aggregated_heatmap.get_model3": 4,  # Professional+
        
        # Futures Orderbook
        "futures.orderbook.get_ask_bids_history": 1,  # All plans
        "futures.orderbook.get_aggregated_ask_bids_history": 1,  # All plans
        "futures.orderbook.get_history": 3,  # Standard+ (was getting Upgrade plan error at level 2)
        "futures.orderbook.get_large_limit_order": 3,  # Standard+
        "futures.orderbook.get_large_limit_order_history": 3,  # Standard+
        
        # Futures Taker Buy/Sell Volume
        "futures.taker_buy_sell_volume.get_history": 1,  # All plans
        "futures.taker_buy_sell_volume.get_exchange_list": 1,  # All plans
        "futures.aggregated_taker_buy_sell_volume.get_history": 1,  # All plans
        
        # Futures Long/Short Ratios
        "futures.global_long_short_account_ratio.get_history": 1,  # All plans
        "futures.top_long_short_account_ratio.get_history": 1,  # All plans
        "futures.top_long_short_position_ratio.get_history": 1,  # All plans
        
        # Futures RSI
        "futures.rsi.get_list": 3,  # Standard+
        
        # Spot endpoints
        "spot.get_supported_coins": 1,  # All plans
        "spot.get_supported_exchange_pairs": 1,  # All plans
        "spot.get_coins_markets": 3,  # Standard+
        "spot.get_pairs_markets": 1,  # All plans
        
        # Spot Price
        "spot.price.get_history": 1,  # All plans (with interval restrictions)
        
        # Spot Orderbook
        "spot.orderbook.get_ask_bids_history": 1,  # All plans
        "spot.orderbook.get_aggregated_ask_bids_history": 1,  # All plans
        "spot.orderbook.get_history": 3,  # Standard+ (was getting Upgrade plan error at level 2)
        "spot.orderbook.get_large_limit_order": 3,  # Standard+
        "spot.orderbook.get_large_limit_order_history": 3,  # Standard+
        
        # Spot Taker Buy/Sell Volume
        "spot.taker_buy_sell_volume.get_history": 1,  # All plans
        "spot.aggregated_taker_buy_sell_volume.get_history": 1,  # All plans
        
        # Options endpoints
        "option.get_max_pain": 1,  # All plans
        "option.get_info": 1,  # All plans
        "option.exchanges.get_list": 1,  # All plans
        "option.gamma.get_exposure": 1,  # All plans
        "option.gamma.get_flow": 1,  # All plans
        "option.open_interest.get_history": 1,  # All plans
        "option.put_call_ratio.get_history": 1,  # All plans
        "option.traders_flow.get_list": 1,  # All plans
        "option.traders_flow_expiry.get_list": 1,  # All plans
        "option.volume.get_history": 1,  # All plans
        "option.volume_strike.get_history": 1,  # All plans
        
        # Exchange/On-chain endpoints
        "exchange.get_assets": 1,  # All plans
        "exchange.balance.get_list": 1,  # All plans
        "exchange.balance.get_chart": 1,  # All plans
        "exchange.chain.tx.get_list": 1,  # All plans
        
        # ETF endpoints
        "etf.bitcoin.get_list": 1,  # All plans
        "etf.bitcoin.get_flow_history": 1,  # All plans
        "etf.bitcoin.get_history": 1,  # All plans
        "etf.bitcoin.get_detail": 1,  # All plans
        "etf.bitcoin.get_aum": 1,  # All plans
        "etf.bitcoin.net_assets.get_history": 1,  # All plans
        "etf.bitcoin.price.get_history": 1,  # All plans
        "etf.bitcoin.premium_discount.get_list": 1,  # All plans
        
        "etf.ethereum.get_list": 1,  # All plans
        "etf.ethereum.get_flow_history": 1,  # All plans
        "etf.ethereum.net_assets.get_history": 1,  # All plans
        
        # Hong Kong ETF
        "hk_etf.bitcoin.get_flow_history": 1,  # All plans
        "hk_etf.ethereum.get_flow_history": 1,  # All plans
        
        # Grayscale
        "grayscale.holdings.get_list": 1,  # All plans
        "grayscale.premium.get_history": 1,  # All plans
        
        # Index/Indicators
        "index.get_fear_greed_history": 1,  # All plans
        "index.get_option_vs_futures_oi_ratio": 1,  # All plans
        "index.get_bitcoin_vs_global_m2_growth": 1,  # All plans
        "index.get_bitcoin_vs_us_m2_growth": 1,  # All plans
        "index.get_ahr999": 1,  # All plans
        "index.get_two_year_ma_multiplier": 1,  # All plans
        "index.get_two_hundred_week_moving_avg_heatmap": 1,  # All plans
        "index.get_altcoin_season_index": 1,  # All plans
        "index.get_bitcoin_short_term_holder_sopr": 1,  # All plans
        "index.get_bitcoin_long_term_holder_sopr": 1,  # All plans
        "index.get_bitcoin_short_term_holder_realized_price": 1,  # All plans
        "index.get_bitcoin_long_term_holder_realized_price": 1,  # All plans
        "index.get_bitcoin_short_term_holder_supply": 1,  # All plans
        "index.get_bitcoin_long_term_holder_supply": 1,  # All plans
        "index.get_bitcoin_rhodl_ratio": 1,  # All plans
        "index.get_bitcoin_reserve_risk": 1,  # All plans
        "index.get_bitcoin_active_addresses": 1,  # All plans
        "index.get_bitcoin_new_addresses": 1,  # All plans
        "index.get_bitcoin_net_unrealized_pnl": 1,  # All plans
        "index.get_btc_correlations": 1,  # All plans
        "index.get_bitcoin_macro_oscillator": 1,  # All plans
        
        # Hyperliquid
        "hyperliquid.get_whale_alert": 1,  # All plans
        "hyperliquid.get_whale_position": 1,  # All plans
        
        # Calendar
        "calendar.get_economic_data": 1,  # All plans
        
        # Top-level indicators
        "get_coinbase_premium_index": 1,  # All plans
        "get_bitfinex_margin_long_short": 1,  # All plans
        "get_borrow_interest_rate_history": 1,  # All plans
        "get_ahr999": 1,  # All plans
        "get_bull_market_peak_indicator": 1,  # All plans
        "get_puell_multiple": 1,  # All plans
        "get_stock_to_flow": 1,  # All plans
        "get_pi_cycle_top_indicator": 1,  # All plans
        "get_golden_ratio_multiplier": 1,  # All plans
        "get_bitcoin_profitable_days": 1,  # All plans
        "get_bitcoin_rainbow_chart": 1,  # All plans
    }
    
    @classmethod
    def get_all_endpoints(cls) -> Dict[str, int]:
        """
        Get all endpoints with their required plan levels.
        
        Returns:
            Dictionary mapping endpoint names to required plan levels
        """
        return cls.ENDPOINTS.copy()
    
    @classmethod
    def get_available_endpoints(cls, plan_level: int) -> List[str]:
        """
        Get list of endpoints available for a given plan level.
        
        Args:
            plan_level: User's plan level (1-5)
            
        Returns:
            List of endpoint names available for the plan level
        """
        return [
            endpoint for endpoint, required_level in cls.ENDPOINTS.items()
            if plan_level >= required_level
        ]
    
    @classmethod
    def check_endpoint_access(cls, endpoint_name: str, plan_level: int) -> bool:
        """
        Check if an endpoint is accessible with a given plan level.
        
        Args:
            endpoint_name: Name of the endpoint to check
            plan_level: User's plan level (1-5)
            
        Returns:
            True if endpoint is accessible, False otherwise
        """
        required_level = cls.ENDPOINTS.get(endpoint_name)
        if required_level is None:
            return False  # Endpoint not found
        return plan_level >= required_level
    
    @classmethod
    def get_endpoint_requirement(cls, endpoint_name: str) -> Optional[int]:
        """
        Get the required plan level for an endpoint.
        
        Args:
            endpoint_name: Name of the endpoint
            
        Returns:
            Required plan level (1-5) or None if endpoint not found
        """
        return cls.ENDPOINTS.get(endpoint_name)
    
    @classmethod
    def get_endpoints_by_level(cls, level: int) -> List[str]:
        """
        Get endpoints that require exactly a specific plan level.
        
        Args:
            level: Plan level (1-5)
            
        Returns:
            List of endpoint names requiring exactly this level
        """
        return [
            endpoint for endpoint, required_level in cls.ENDPOINTS.items()
            if required_level == level
        ]
    
    @classmethod
    def get_statistics(cls) -> Dict[str, any]:
        """
        Get statistics about endpoint distribution across plan levels.
        
        Returns:
            Dictionary with statistics
        """
        total = len(cls.ENDPOINTS)
        by_level = {}
        for level in range(1, 6):
            count = len([e for e, l in cls.ENDPOINTS.items() if l == level])
            by_level[PlanLevel.get_name(level)] = count
        
        return {
            "total_endpoints": total,
            "by_plan_level": by_level,
            "free_endpoints": len([e for e, l in cls.ENDPOINTS.items() if l == 1]),
            "premium_endpoints": len([e for e, l in cls.ENDPOINTS.items() if l > 1]),
        }


# Convenience functions
def get_available_endpoints(plan_level: int) -> List[str]:
    """Get list of endpoints available for a given plan level."""
    return EndpointRegistry.get_available_endpoints(plan_level)


def check_endpoint_access(endpoint_name: str, plan_level: int) -> bool:
    """Check if an endpoint is accessible with a given plan level."""
    return EndpointRegistry.check_endpoint_access(endpoint_name, plan_level)


def get_all_endpoints() -> Dict[str, int]:
    """Get all endpoints with their required plan levels."""
    return EndpointRegistry.get_all_endpoints()