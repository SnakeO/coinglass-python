#!/usr/bin/env python3
"""
Comprehensive test for ALL CoinGlass API endpoints
Tests all 116 endpoints and outputs results in a table format with plan availability info
"""
import os
import sys
import json
import time
import traceback
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
from pathlib import Path
import re
from dotenv import load_dotenv
from urllib.parse import urljoin

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from coinglass import CoinGlass
from coinglass.constants import PlanLevel
from coinglass.endpoints import EndpointRegistry

# Load environment variables
load_dotenv()

# Use the endpoint registry to get plan requirements
ENDPOINT_REGISTRY = EndpointRegistry()


class EndpointTester:
    """Test all CoinGlass API endpoints comprehensively."""
    
    def __init__(self, api_key: str = None, plan_level: int = None):
        """Initialize the tester with API key and plan level."""
        self.api_key = api_key or os.getenv('CG_API_KEY')
        if not self.api_key:
            raise ValueError("API key required. Set CG_API_KEY in .env file")
        
        # Get plan level from environment or default to 1 (Hobbyist)
        self.plan_level = plan_level or int(os.getenv('PLAN_LEVEL', '1'))
        if self.plan_level < 1 or self.plan_level > 5:
            raise ValueError(f"Invalid PLAN_LEVEL: {self.plan_level}. Must be between 1-5")
        
        print(f"\nTesting with Plan Level: {self.plan_level} ({PlanLevel.get_name(self.plan_level)})")
        
        # Get available endpoints for this plan level
        self.available_endpoints = ENDPOINT_REGISTRY.get_available_endpoints(self.plan_level)
        total_endpoints = len(ENDPOINT_REGISTRY.get_all_endpoints())
        print(f"Available endpoints: {len(self.available_endpoints)} out of {total_endpoints} total")
        
        self.cg = CoinGlass(api_key=self.api_key)
        self.results = []
        self.test_count = 0
        self.rate_limit_wait = 0  # Dynamic rate limit wait time
        self.last_request_time = 0
    
    def test_endpoint(self, name: str, func: callable, params: Dict = None) -> Tuple[str, str, str, str, str, int]:
        """
        Test a single endpoint and return results.
        
        Args:
            name: Endpoint name
            func: Function to call
            params: Parameters to pass
        
        Returns:
            Tuple of (endpoint_name, url, plan_required, params_str, status, result_str)
        """
        self.test_count += 1
        print(".", end="", flush=True)
        if self.test_count % 10 == 0:
            print(f" [{self.test_count}/118]", end="", flush=True)
        if self.test_count % 50 == 0:
            print()  # New line every 50 tests
        
        params = params or {}
        params_str = json.dumps(params) if params else "None"
        
        # Construct the URL based on the endpoint name
        url = self._construct_url(name)
        
        # Get plan requirement for this endpoint
        required_level = ENDPOINT_REGISTRY.get_endpoint_requirement(name)
        plan_required = f"Level {required_level}" if required_level else "Unknown"
        
        # Check if user has access to this endpoint
        if required_level and self.plan_level < required_level:
            status = "⏭️ SKIPPED"
            result_str = f"Requires plan level {required_level} ({PlanLevel.get_name(required_level)})"
            return name, url, plan_required, params_str, status, result_str
        
        try:
            # Smart rate limiting - wait if needed
            if self.rate_limit_wait > 0:
                time.sleep(self.rate_limit_wait)
                self.rate_limit_wait = max(0, self.rate_limit_wait - 0.5)  # Gradually reduce wait time
            
            # Minimum time between requests
            time_since_last = time.time() - self.last_request_time
            if time_since_last < 0.5:
                time.sleep(0.5 - time_since_last)
            
            self.last_request_time = time.time()
            
            # Call the endpoint
            result = func(**params) if params else func()
            
            # Format result for display
            if isinstance(result, (dict, list)):
                if isinstance(result, list) and len(result) > 0:
                    # For lists, show first item and count
                    first_item = json.dumps(result[0] if result else {}, indent=2)[:200]
                    result_str = f"List[{len(result)}]: {first_item}..."
                elif isinstance(result, dict):
                    # For dicts, show truncated version
                    result_str = json.dumps(result, indent=2)[:200] + "..."
                else:
                    result_str = str(result)[:200]
            else:
                result_str = str(result)[:200]
            
            status = "✅ SUCCESS"
            self.rate_limit_wait = max(0, self.rate_limit_wait - 0.5)  # Success reduces wait time
            
        except Exception as e:
            error_msg = str(e)
            
            # Check for rate limiting (429 status)
            if "429" in error_msg or "Too Many Requests" in error_msg or "rate limit" in error_msg.lower():
                # Exponential backoff for rate limiting
                self.rate_limit_wait = min(self.rate_limit_wait * 2 + 2, 30)  # Max 30 second wait
                print(f"\n⏸️  Rate limited. Waiting {self.rate_limit_wait:.1f}s...", end="", flush=True)
                time.sleep(self.rate_limit_wait)
                # Retry once after rate limit
                try:
                    result = func(**params) if params else func()
                    status = "✅ SUCCESS (after retry)"
                    result_str = "Success after rate limit retry"
                except Exception as retry_e:
                    result_str = f"❌ ERROR: {str(retry_e)[:150]}"
                    status = "❌ FAILED"
            else:
                result_str = f"❌ ERROR: {error_msg[:150]}"
                status = "❌ FAILED"
        
        return name, url, plan_required, params_str, status, result_str
    
    def _construct_url(self, endpoint_name: str) -> str:
        """Construct the actual API URL from endpoint name."""
        base_url = "https://open-api-v4.coinglass.com/api"
        
        # Map endpoint names to actual API paths
        path_mapping = {
            # Futures endpoints
            "futures.get_supported_coins": "/futures/supported-coins",
            "futures.get_supported_exchange_pairs": "/futures/supported-exchange-pairs",
            "futures.get_coins_markets": "/futures/coins-markets",
            "futures.get_pairs_markets": "/futures/pairs-markets",
            "futures.get_coins_price_change": "/futures/coins-price-change",
            "futures.get_delisted_pairs": "/futures/delisted-exchange-pairs",
            "futures.get_exchange_rank": "/futures/exchange-rank",
            "futures.get_basis": "/futures/basis/history",
            "futures.get_whale_index": "/futures/whale-index/history",
            "futures.get_cgdi_index": "/futures/cgdi-index/history",
            "futures.get_cdri_index": "/futures/cdri-index/history",
            "futures.price.get_history": "/futures/price/history",
            "futures.open_interest.get_history": "/futures/open-interest/history",
            "futures.open_interest.get_aggregated_history": "/futures/aggregated-open-interest/history",
            "futures.open_interest.get_aggregated_stablecoin_margin_history": "/futures/aggregated-stablecoin-margin-open-interest/history",
            "futures.open_interest.get_aggregated_coin_margin_history": "/futures/aggregated-coin-margin-open-interest/history",
            "futures.open_interest.get_exchange_list": "/futures/open-interest/exchange-list",
            "futures.open_interest.get_exchange_history_chart": "/futures/open-interest/exchange-history-chart",
            "futures.funding_rate.get_history": "/futures/funding-rate/history",
            "futures.funding_rate.get_oi_weight_history": "/futures/oi-weight-funding-rate/history",
            "futures.funding_rate.get_vol_weight_history": "/futures/vol-weight-funding-rate/history",
            "futures.funding_rate.get_exchange_list": "/futures/funding-rate/exchange-list",
            "futures.funding_rate.get_accumulated_exchange_list": "/futures/accumulated-funding-rate/exchange-list",
            "futures.funding_rate.get_arbitrage": "/futures/funding-rate-arbitrage",
            "futures.global_long_short_account_ratio.get_history": "/futures/global-long-short-account-ratio/history",
            "futures.top_long_short_account_ratio.get_history": "/futures/top-long-short-account-ratio/history",
            "futures.top_long_short_position_ratio.get_history": "/futures/top-long-short-position-ratio/history",
            "futures.liquidation.get_history": "/futures/liquidation/history",
            "futures.liquidation.get_aggregated_history": "/futures/aggregated-liquidation/history",
            "futures.liquidation.get_coin_list": "/futures/liquidation/coin-list",
            "futures.liquidation.get_exchange_list": "/futures/liquidation/exchange-list",
            "futures.liquidation.get_order": "/futures/liquidation-order",
            "futures.liquidation.get_map": "/futures/liquidation-map",
            "futures.liquidation.get_aggregated_map": "/futures/aggregated-liquidation-map",
            "futures.liquidation.heatmap.get_model1": "/futures/liquidation-heatmap-model1",
            "futures.liquidation.heatmap.get_model2": "/futures/liquidation-heatmap-model2",
            "futures.liquidation.heatmap.get_model3": "/futures/liquidation-heatmap-model3",
            "futures.liquidation.aggregated_heatmap.get_model1": "/futures/aggregated-liquidation-heatmap-model1",
            "futures.liquidation.aggregated_heatmap.get_model2": "/futures/aggregated-liquidation-heatmap-model2",
            "futures.liquidation.aggregated_heatmap.get_model3": "/futures/aggregated-liquidation-heatmap-model3",
            "futures.orderbook.get_ask_bids_history": "/futures/orderbook-ask-bids/history",
            "futures.orderbook.get_aggregated_ask_bids_history": "/futures/aggregated-orderbook-ask-bids/history",
            "futures.orderbook.get_history": "/futures/orderbook/history",
            "futures.orderbook.get_large_limit_order": "/futures/large-limit-order",
            "futures.orderbook.get_large_limit_order_history": "/futures/large-limit-order/history",
            "futures.taker_buy_sell_volume.get_history": "/futures/taker-buy-sell-volume/history",
            "futures.taker_buy_sell_volume.get_exchange_list": "/futures/taker-buy-sell-volume/exchange-list",
            "futures.aggregated_taker_buy_sell_volume.get_history": "/futures/aggregated-taker-buy-sell-volume/history",
            "futures.rsi.get_list": "/futures/rsi-list",
            # Spot endpoints
            "spot.get_supported_coins": "/spot/supported-coins",
            "spot.get_supported_exchange_pairs": "/spot/supported-exchange-pairs",
            "spot.get_coins_markets": "/spot/coins-markets",
            "spot.get_pairs_markets": "/spot/pairs-markets",
            "spot.price.get_history": "/spot/price/history",
            "spot.orderbook.get_ask_bids_history": "/spot/orderbook-ask-bids/history",
            "spot.orderbook.get_aggregated_ask_bids_history": "/spot/aggregated-orderbook-ask-bids/history",
            "spot.orderbook.get_history": "/spot/orderbook/history",
            "spot.orderbook.get_large_limit_order": "/spot/large-limit-order",
            "spot.orderbook.get_large_limit_order_history": "/spot/large-limit-order/history",
            "spot.taker_buy_sell_volume.get_history": "/spot/taker-buy-sell-volume/history",
            "spot.aggregated_taker_buy_sell_volume.get_history": "/spot/aggregated-taker-buy-sell-volume/history",
            # Options
            "option.get_max_pain": "/option/max-pain",
            "option.get_info": "/option/info",
            "option.get_exchange_oi_history": "/option/exchange-oi/history",
            "option.get_exchange_vol_history": "/option/exchange-vol/history",
            # Exchange/On-chain
            "exchange.get_assets": "/exchange/assets",
            "exchange.balance.get_list": "/exchange/balance-list",
            "exchange.balance.get_chart": "/exchange/balance-chart",
            "exchange.chain.tx.get_list": "/exchange/chain-tx-list",
            # ETF
            "etf.bitcoin.get_list": "/etf/bitcoin/list",
            "etf.bitcoin.net_assets.get_history": "/etf/bitcoin/net-assets/history",
            "etf.bitcoin.get_flow_history": "/etf/bitcoin/flow/history",
            "etf.bitcoin.premium_discount.get_history": "/etf/bitcoin/premium-discount/history",
            "etf.bitcoin.get_history": "/etf/bitcoin/history",
            "etf.bitcoin.price.get_history": "/etf/bitcoin/price/history",
            "etf.bitcoin.get_detail": "/etf/bitcoin/detail",
            "etf.bitcoin.get_aum": "/etf/bitcoin/aum",
            "etf.ethereum.get_list": "/etf/ethereum/list",
            "etf.ethereum.net_assets.get_history": "/etf/ethereum/net-assets/history",
            "etf.ethereum.get_flow_history": "/etf/ethereum/flow/history",
            "hk_etf.bitcoin.get_flow_history": "/hk-etf/bitcoin/flow/history",
            # Grayscale
            "grayscale.holdings.get_list": "/grayscale/holdings-list",
            "grayscale.premium.get_history": "/grayscale/premium/history",
            # Hyperliquid
            "hyperliquid.get_whale_alert": "/hyperliquid/whale-alert",
            "hyperliquid.get_whale_position": "/hyperliquid/whale-position",
            # Index/Indicators
            "index.get_fear_greed_history": "/index/fear-greed/history",
            "index.get_option_vs_futures_oi_ratio": "/index/option-vs-futures-oi-ratio",
            "index.get_bitcoin_vs_global_m2_growth": "/index/bitcoin-vs-global-m2-growth",
            "index.get_bitcoin_vs_us_m2_growth": "/index/bitcoin-vs-us-m2-growth",
            "index.get_ahr999": "/index/ahr999",
            "index.get_two_year_ma_multiplier": "/index/two-year-ma-multiplier",
            "index.get_two_hundred_week_moving_avg_heatmap": "/index/two-hundred-week-moving-avg-heatmap",
            "index.get_altcoin_season_index": "/index/altcoin-season-index",
            "index.get_bitcoin_short_term_holder_sopr": "/index/bitcoin-short-term-holder-sopr",
            "index.get_bitcoin_long_term_holder_sopr": "/index/bitcoin-long-term-holder-sopr",
            "index.get_bitcoin_short_term_holder_realized_price": "/index/bitcoin-short-term-holder-realized-price",
            "index.get_bitcoin_long_term_holder_realized_price": "/index/bitcoin-long-term-holder-realized-price",
            "index.get_bitcoin_short_term_holder_supply": "/index/bitcoin-short-term-holder-supply",
            "index.get_bitcoin_long_term_holder_supply": "/index/bitcoin-long-term-holder-supply",
            "index.get_bitcoin_rhodl_ratio": "/index/bitcoin-rhodl-ratio",
            "index.get_bitcoin_reserve_risk": "/index/bitcoin-reserve-risk",
            "index.get_bitcoin_active_addresses": "/index/bitcoin-active-addresses",
            "index.get_bitcoin_new_addresses": "/index/bitcoin-new-addresses",
            "index.get_bitcoin_net_unrealized_pnl": "/index/bitcoin-net-unrealized-pnl",
            "index.get_btc_correlations": "/index/btc-correlations",
            "index.get_bitcoin_macro_oscillator": "/index/bitcoin-macro-oscillator",
            # Calendar
            "calendar.get_economic_data": "/calendar/economic-data",
            # Top-level indicators
            "get_coinbase_premium_index": "/index/coinbase-premium-index",
            "get_bitfinex_margin_long_short": "/index/bitfinex-margin-long-short",
            "get_borrow_interest_rate_history": "/index/borrow-interest-rate/history",
            "get_ahr999": "/index/ahr999",
            "get_bull_market_peak_indicator": "/index/bull-market-peak-indicator",
            "get_puell_multiple": "/index/puell-multiple",
            "get_stock_to_flow": "/index/stock-to-flow",
            "get_pi_cycle_top_indicator": "/index/pi-cycle-top-indicator",
            "get_golden_ratio_multiplier": "/index/golden-ratio-multiplier",
            "get_bitcoin_profitable_days": "/index/bitcoin-profitable-days",
            "get_bitcoin_rainbow_chart": "/index/bitcoin-rainbow-chart"
        }
        
        path = path_mapping.get(endpoint_name, f"/{endpoint_name.replace('.', '/')}")
        return urljoin(base_url, path)
    
    def test_all_futures_endpoints(self):
        """Test all futures endpoints."""
        print("\n🔄 Testing FUTURES endpoints", end="")
        
        # Basic endpoints
        self.results.append(self.test_endpoint(
            "futures.get_supported_coins",
            self.cg.futures.get_supported_coins
        ))
        
        self.results.append(self.test_endpoint(
            "futures.get_supported_exchange_pairs",
            self.cg.futures.get_supported_exchange_pairs
        ))
        
        self.results.append(self.test_endpoint(
            "futures.get_coins_markets",
            self.cg.futures.get_coins_markets
        ))
        
        self.results.append(self.test_endpoint(
            "futures.get_pairs_markets",
            self.cg.futures.get_pairs_markets,
            {"symbol": "BTC"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.get_coins_price_change",
            self.cg.futures.get_coins_price_change
        ))
        
        self.results.append(self.test_endpoint(
            "futures.get_delisted_pairs",
            self.cg.futures.get_delisted_pairs
        ))
        
        self.results.append(self.test_endpoint(
            "futures.get_exchange_rank",
            self.cg.futures.get_exchange_rank
        ))
        
        self.results.append(self.test_endpoint(
            "futures.get_basis",
            self.cg.futures.get_basis,
            {"symbol": "BTC"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.get_whale_index",
            self.cg.futures.get_whale_index
        ))
        
        self.results.append(self.test_endpoint(
            "futures.get_cgdi_index",
            self.cg.futures.get_cgdi_index
        ))
        
        self.results.append(self.test_endpoint(
            "futures.get_cdri_index",
            self.cg.futures.get_cdri_index
        ))
        
        # Price endpoints
        self.results.append(self.test_endpoint(
            "futures.price.get_history",
            self.cg.futures.price.get_history,
            {"symbol": "BTC", "exchange": "Binance", "interval": "1h"}
        ))
        
        # Open Interest endpoints
        self.results.append(self.test_endpoint(
            "futures.open_interest.get_history",
            self.cg.futures.open_interest.get_history,
            {"exchange": "Binance", "symbol": "BTC", "interval": "4h"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.open_interest.get_aggregated_history",
            self.cg.futures.open_interest.get_aggregated_history,
            {"exchange_list": "Binance,OKX", "symbol": "BTC", "interval": "1d"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.open_interest.get_aggregated_stablecoin_margin_history",
            self.cg.futures.open_interest.get_aggregated_stablecoin_margin_history,
            {"symbol": "BTC", "exchange_list": "Binance,OKX", "interval": "4h"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.open_interest.get_aggregated_coin_margin_history",
            self.cg.futures.open_interest.get_aggregated_coin_margin_history,
            {"symbol": "BTC", "exchange_list": "Binance,OKX", "interval": "4h"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.open_interest.get_exchange_list",
            self.cg.futures.open_interest.get_exchange_list,
            {"symbol": "BTC"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.open_interest.get_exchange_history_chart",
            self.cg.futures.open_interest.get_exchange_history_chart,
            {"symbol": "BTC", "range": "1d"}
        ))
        
        # Funding Rate endpoints
        self.results.append(self.test_endpoint(
            "futures.funding_rate.get_history",
            self.cg.futures.funding_rate.get_history,
            {"exchange": "Binance", "symbol": "BTC", "interval": "8h"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.funding_rate.get_oi_weight_history",
            self.cg.futures.funding_rate.get_oi_weight_history,
            {"symbol": "BTC", "interval": "8h"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.funding_rate.get_vol_weight_history",
            self.cg.futures.funding_rate.get_vol_weight_history,
            {"symbol": "BTC", "interval": "8h"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.funding_rate.get_exchange_list",
            self.cg.futures.funding_rate.get_exchange_list,
            {"symbol": "BTC"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.funding_rate.get_accumulated_exchange_list",
            self.cg.futures.funding_rate.get_accumulated_exchange_list,
            {"range": "1d"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.funding_rate.get_arbitrage",
            self.cg.futures.funding_rate.get_arbitrage,
            {"symbol": "BTC"}
        ))
        
        # Long/Short Ratios
        self.results.append(self.test_endpoint(
            "futures.global_long_short_account_ratio.get_history",
            self.cg.futures.global_long_short_account_ratio.get_history,
            {"exchange": "Binance", "symbol": "BTC", "interval": "1h"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.top_long_short_account_ratio.get_history",
            self.cg.futures.top_long_short_account_ratio.get_history,
            {"exchange": "Binance", "symbol": "BTC", "interval": "1h"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.top_long_short_position_ratio.get_history",
            self.cg.futures.top_long_short_position_ratio.get_history,
            {"exchange": "Binance", "symbol": "BTC", "interval": "1h"}
        ))
        
        # Liquidation endpoints
        self.results.append(self.test_endpoint(
            "futures.liquidation.get_history",
            self.cg.futures.liquidation.get_history,
            {"exchange": "Binance", "symbol": "BTC", "interval": "1h"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.liquidation.get_aggregated_history",
            self.cg.futures.liquidation.get_aggregated_history,
            {"symbol": "BTC", "exchange_list": "Binance,OKX", "interval": "1h"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.liquidation.get_coin_list",
            self.cg.futures.liquidation.get_coin_list
        ))
        
        self.results.append(self.test_endpoint(
            "futures.liquidation.get_exchange_list",
            self.cg.futures.liquidation.get_exchange_list,
            {"range": "1h"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.liquidation.get_order",
            self.cg.futures.liquidation.get_order,
            {"exchange": "Binance", "symbol": "BTCUSDT"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.liquidation.get_map",
            self.cg.futures.liquidation.get_map,
            {"exchange": "Binance", "symbol": "BTCUSDT"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.liquidation.get_aggregated_map",
            self.cg.futures.liquidation.get_aggregated_map,
            {"symbol": "BTC"}
        ))
        
        # Liquidation Heatmaps
        self.results.append(self.test_endpoint(
            "futures.liquidation.heatmap.get_model1",
            self.cg.futures.liquidation.heatmap.get_model1,
            {"exchange": "Binance", "symbol": "BTCUSDT"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.liquidation.heatmap.get_model2",
            self.cg.futures.liquidation.heatmap.get_model2,
            {"exchange": "Binance", "symbol": "BTCUSDT"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.liquidation.heatmap.get_model3",
            self.cg.futures.liquidation.heatmap.get_model3,
            {"exchange": "Binance", "symbol": "BTCUSDT"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.liquidation.aggregated_heatmap.get_model1",
            self.cg.futures.liquidation.aggregated_heatmap.get_model1,
            {"symbol": "BTC"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.liquidation.aggregated_heatmap.get_model2",
            self.cg.futures.liquidation.aggregated_heatmap.get_model2,
            {"symbol": "BTC"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.liquidation.aggregated_heatmap.get_model3",
            self.cg.futures.liquidation.aggregated_heatmap.get_model3,
            {"symbol": "BTC"}
        ))
        
        # Orderbook endpoints
        self.results.append(self.test_endpoint(
            "futures.orderbook.get_ask_bids_history",
            self.cg.futures.orderbook.get_ask_bids_history,
            {"exchange": "Binance", "symbol": "BTC", "interval": "1h"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.orderbook.get_aggregated_ask_bids_history",
            self.cg.futures.orderbook.get_aggregated_ask_bids_history,
            {"symbol": "BTC", "exchange_list": "Binance,OKX", "interval": "1h"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.orderbook.get_history",
            self.cg.futures.orderbook.get_history,
            {"exchange": "Binance", "symbol": "BTC", "interval": "1h"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.orderbook.get_large_limit_order",
            self.cg.futures.orderbook.get_large_limit_order,
            {"exchange": "Binance", "symbol": "BTCUSDT"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.orderbook.get_large_limit_order_history",
            self.cg.futures.orderbook.get_large_limit_order_history,
            {"exchange": "Binance", "symbol": "BTCUSDT", "interval": "1h"}
        ))
        
        # Taker Buy/Sell Volume
        self.results.append(self.test_endpoint(
            "futures.taker_buy_sell_volume.get_history",
            self.cg.futures.taker_buy_sell_volume.get_history,
            {"exchange": "Binance", "symbol": "BTC", "interval": "1h"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.taker_buy_sell_volume.get_exchange_list",
            self.cg.futures.taker_buy_sell_volume.get_exchange_list,
            {"symbol": "BTC"}
        ))
        
        self.results.append(self.test_endpoint(
            "futures.aggregated_taker_buy_sell_volume.get_history",
            self.cg.futures.aggregated_taker_buy_sell_volume.get_history,
            {"symbol": "BTC", "exchange_list": "Binance,OKX", "interval": "1h"}
        ))
        
        # RSI
        self.results.append(self.test_endpoint(
            "futures.rsi.get_list",
            self.cg.futures.rsi.get_list
        ))
    
    def test_all_spot_endpoints(self):
        """Test all spot endpoints."""
        print("\n🔄 Testing SPOT endpoints", end="")
        
        self.results.append(self.test_endpoint(
            "spot.get_supported_coins",
            self.cg.spot.get_supported_coins
        ))
        
        self.results.append(self.test_endpoint(
            "spot.get_supported_exchange_pairs",
            self.cg.spot.get_supported_exchange_pairs
        ))
        
        self.results.append(self.test_endpoint(
            "spot.get_coins_markets",
            self.cg.spot.get_coins_markets
        ))
        
        self.results.append(self.test_endpoint(
            "spot.get_pairs_markets",
            self.cg.spot.get_pairs_markets,
            {"symbol": "BTC"}
        ))
        
        self.results.append(self.test_endpoint(
            "spot.price.get_history",
            self.cg.spot.price.get_history,
            {"symbol": "BTC/USDT", "exchange": "Binance", "interval": "1h"}
        ))
        
        self.results.append(self.test_endpoint(
            "spot.orderbook.get_ask_bids_history",
            self.cg.spot.orderbook.get_ask_bids_history,
            {"exchange": "Binance", "symbol": "BTC/USDT", "interval": "1h"}
        ))
        
        self.results.append(self.test_endpoint(
            "spot.orderbook.get_aggregated_ask_bids_history",
            self.cg.spot.orderbook.get_aggregated_ask_bids_history,
            {"exchange_list": "Binance,OKX", "symbol": "BTC", "interval": "1h"}
        ))
        
        self.results.append(self.test_endpoint(
            "spot.orderbook.get_history",
            self.cg.spot.orderbook.get_history,
            {"exchange": "Binance", "symbol": "BTC/USDT"}
        ))
        
        self.results.append(self.test_endpoint(
            "spot.orderbook.get_large_limit_order",
            self.cg.spot.orderbook.get_large_limit_order,
            {"exchange": "Binance", "symbol": "BTC/USDT"}
        ))
        
        self.results.append(self.test_endpoint(
            "spot.orderbook.get_large_limit_order_history",
            self.cg.spot.orderbook.get_large_limit_order_history,
            {"exchange": "Binance", "symbol": "BTC/USDT"}
        ))
        
        self.results.append(self.test_endpoint(
            "spot.taker_buy_sell_volume.get_history",
            self.cg.spot.taker_buy_sell_volume.get_history,
            {"exchange": "Binance", "symbol": "BTC/USDT", "interval": "1h"}
        ))
        
        self.results.append(self.test_endpoint(
            "spot.aggregated_taker_buy_sell_volume.get_history",
            self.cg.spot.aggregated_taker_buy_sell_volume.get_history,
            {"exchange_list": "Binance,OKX", "symbol": "BTC", "interval": "1h"}
        ))
    
    def test_all_option_endpoints(self):
        """Test all option endpoints."""
        print("\n🔄 Testing OPTION endpoints", end="")
        
        self.results.append(self.test_endpoint(
            "option.get_max_pain",
            self.cg.option.get_max_pain,
            {"symbol": "BTC", "exchange": "Deribit"}
        ))
        
        self.results.append(self.test_endpoint(
            "option.get_info",
            self.cg.option.get_info,
            {"symbol": "BTC"}
        ))
        
        self.results.append(self.test_endpoint(
            "option.get_exchange_oi_history",
            self.cg.option.get_exchange_oi_history,
            {"symbol": "BTC", "unit": "USD", "range": "1d"}
        ))
        
        self.results.append(self.test_endpoint(
            "option.get_exchange_vol_history",
            self.cg.option.get_exchange_vol_history,
            {"symbol": "BTC", "unit": "USD", "range": "1d"}
        ))
    
    def test_all_exchange_endpoints(self):
        """Test all exchange/on-chain endpoints."""
        print("\n🔄 Testing EXCHANGE/ON-CHAIN endpoints", end="")
        
        self.results.append(self.test_endpoint(
            "exchange.get_assets",
            self.cg.exchange.get_assets,
            {"exchange": "Binance"}
        ))
        
        self.results.append(self.test_endpoint(
            "exchange.balance.get_list",
            self.cg.exchange.balance.get_list,
            {"symbol": "BTC"}
        ))
        
        self.results.append(self.test_endpoint(
            "exchange.balance.get_chart",
            self.cg.exchange.balance.get_chart,
            {"symbol": "BTC"}
        ))
        
        self.results.append(self.test_endpoint(
            "exchange.chain.tx.get_list",
            self.cg.exchange.chain.tx.get_list,
            {"exchange": "Binance"}
        ))
    
    def test_all_etf_endpoints(self):
        """Test all ETF endpoints."""
        print("\n🔄 Testing ETF endpoints", end="")
        
        # Bitcoin ETF
        self.results.append(self.test_endpoint(
            "etf.bitcoin.get_list",
            self.cg.etf.bitcoin.get_list
        ))
        
        self.results.append(self.test_endpoint(
            "etf.bitcoin.net_assets.get_history",
            self.cg.etf.bitcoin.net_assets.get_history
        ))
        
        self.results.append(self.test_endpoint(
            "etf.bitcoin.get_flow_history",
            self.cg.etf.bitcoin.get_flow_history
        ))
        
        self.results.append(self.test_endpoint(
            "etf.bitcoin.premium_discount.get_history",
            self.cg.etf.bitcoin.premium_discount.get_history
        ))
        
        self.results.append(self.test_endpoint(
            "etf.bitcoin.get_history",
            self.cg.etf.bitcoin.get_history,
            {"ticker": "GBTC"}
        ))
        
        self.results.append(self.test_endpoint(
            "etf.bitcoin.price.get_history",
            self.cg.etf.bitcoin.price.get_history,
            {"ticker": "GBTC", "range": "7d"}
        ))
        
        self.results.append(self.test_endpoint(
            "etf.bitcoin.get_detail",
            self.cg.etf.bitcoin.get_detail,
            {"ticker": "GBTC"}
        ))
        
        self.results.append(self.test_endpoint(
            "etf.bitcoin.get_aum",
            self.cg.etf.bitcoin.get_aum
        ))
        
        # Ethereum ETF
        self.results.append(self.test_endpoint(
            "etf.ethereum.get_list",
            self.cg.etf.ethereum.get_list
        ))
        
        self.results.append(self.test_endpoint(
            "etf.ethereum.net_assets.get_history",
            self.cg.etf.ethereum.net_assets.get_history
        ))
        
        self.results.append(self.test_endpoint(
            "etf.ethereum.get_flow_history",
            self.cg.etf.ethereum.get_flow_history
        ))
        
        # HK ETF
        self.results.append(self.test_endpoint(
            "hk_etf.bitcoin.get_flow_history",
            self.cg.hk_etf.bitcoin.get_flow_history
        ))
    
    def test_all_grayscale_endpoints(self):
        """Test all Grayscale endpoints."""
        print("\n🔄 Testing GRAYSCALE endpoints", end="")
        
        self.results.append(self.test_endpoint(
            "grayscale.holdings.get_list",
            self.cg.grayscale.holdings.get_list
        ))
        
        self.results.append(self.test_endpoint(
            "grayscale.premium.get_history",
            self.cg.grayscale.premium.get_history
        ))
    
    def test_all_hyperliquid_endpoints(self):
        """Test all Hyperliquid endpoints."""
        print("\n🔄 Testing HYPERLIQUID endpoints", end="")
        
        self.results.append(self.test_endpoint(
            "hyperliquid.get_whale_alert",
            self.cg.hyperliquid.get_whale_alert
        ))
        
        self.results.append(self.test_endpoint(
            "hyperliquid.get_whale_position",
            self.cg.hyperliquid.get_whale_position
        ))
    
    def test_all_index_endpoints(self):
        """Test all index/indicator endpoints."""
        print("\n🔄 Testing INDEX/INDICATOR endpoints", end="")
        
        self.results.append(self.test_endpoint(
            "index.get_fear_greed_history",
            self.cg.index.get_fear_greed_history
        ))
        
        self.results.append(self.test_endpoint(
            "index.get_option_vs_futures_oi_ratio",
            self.cg.index.get_option_vs_futures_oi_ratio
        ))
        
        self.results.append(self.test_endpoint(
            "index.get_bitcoin_vs_global_m2_growth",
            self.cg.index.get_bitcoin_vs_global_m2_growth
        ))
        
        self.results.append(self.test_endpoint(
            "index.get_bitcoin_vs_us_m2_growth",
            self.cg.index.get_bitcoin_vs_us_m2_growth
        ))
        
        self.results.append(self.test_endpoint(
            "index.get_ahr999",
            self.cg.index.get_ahr999
        ))
        
        self.results.append(self.test_endpoint(
            "index.get_two_year_ma_multiplier",
            self.cg.index.get_two_year_ma_multiplier
        ))
        
        self.results.append(self.test_endpoint(
            "index.get_two_hundred_week_moving_avg_heatmap",
            self.cg.index.get_two_hundred_week_moving_avg_heatmap
        ))
        
        self.results.append(self.test_endpoint(
            "index.get_altcoin_season_index",
            self.cg.index.get_altcoin_season_index
        ))
        
        self.results.append(self.test_endpoint(
            "index.get_bitcoin_short_term_holder_sopr",
            self.cg.index.get_bitcoin_short_term_holder_sopr
        ))
        
        self.results.append(self.test_endpoint(
            "index.get_bitcoin_long_term_holder_sopr",
            self.cg.index.get_bitcoin_long_term_holder_sopr
        ))
        
        self.results.append(self.test_endpoint(
            "index.get_bitcoin_short_term_holder_realized_price",
            self.cg.index.get_bitcoin_short_term_holder_realized_price
        ))
        
        self.results.append(self.test_endpoint(
            "index.get_bitcoin_long_term_holder_realized_price",
            self.cg.index.get_bitcoin_long_term_holder_realized_price
        ))
        
        self.results.append(self.test_endpoint(
            "index.get_bitcoin_short_term_holder_supply",
            self.cg.index.get_bitcoin_short_term_holder_supply
        ))
        
        self.results.append(self.test_endpoint(
            "index.get_bitcoin_long_term_holder_supply",
            self.cg.index.get_bitcoin_long_term_holder_supply
        ))
        
        self.results.append(self.test_endpoint(
            "index.get_bitcoin_rhodl_ratio",
            self.cg.index.get_bitcoin_rhodl_ratio
        ))
        
        self.results.append(self.test_endpoint(
            "index.get_bitcoin_reserve_risk",
            self.cg.index.get_bitcoin_reserve_risk
        ))
        
        self.results.append(self.test_endpoint(
            "index.get_bitcoin_active_addresses",
            self.cg.index.get_bitcoin_active_addresses
        ))
        
        self.results.append(self.test_endpoint(
            "index.get_bitcoin_new_addresses",
            self.cg.index.get_bitcoin_new_addresses
        ))
        
        self.results.append(self.test_endpoint(
            "index.get_bitcoin_net_unrealized_pnl",
            self.cg.index.get_bitcoin_net_unrealized_pnl
        ))
        
        self.results.append(self.test_endpoint(
            "index.get_btc_correlations",
            self.cg.index.get_btc_correlations
        ))
        
        self.results.append(self.test_endpoint(
            "index.get_bitcoin_macro_oscillator",
            self.cg.index.get_bitcoin_macro_oscillator
        ))
    
    def test_all_calendar_endpoints(self):
        """Test calendar endpoints."""
        print("\n🔄 Testing CALENDAR endpoints", end="")
        
        self.results.append(self.test_endpoint(
            "calendar.get_economic_data",
            self.cg.calendar.get_economic_data
        ))
    
    def test_all_toplevel_endpoints(self):
        """Test all top-level indicator endpoints."""
        print("\n🔄 Testing TOP-LEVEL INDICATOR endpoints", end="")
        
        self.results.append(self.test_endpoint(
            "get_coinbase_premium_index",
            self.cg.get_coinbase_premium_index
        ))
        
        self.results.append(self.test_endpoint(
            "get_bitfinex_margin_long_short",
            self.cg.get_bitfinex_margin_long_short,
            {"symbol": "BTC", "interval": "1d"}
        ))
        
        self.results.append(self.test_endpoint(
            "get_borrow_interest_rate_history",
            self.cg.get_borrow_interest_rate_history,
            {"symbol": "BTC"}
        ))
        
        self.results.append(self.test_endpoint(
            "get_ahr999",
            self.cg.get_ahr999
        ))
        
        self.results.append(self.test_endpoint(
            "get_bull_market_peak_indicator",
            self.cg.get_bull_market_peak_indicator
        ))
        
        self.results.append(self.test_endpoint(
            "get_puell_multiple",
            self.cg.get_puell_multiple
        ))
        
        self.results.append(self.test_endpoint(
            "get_stock_to_flow",
            self.cg.get_stock_to_flow
        ))
        
        self.results.append(self.test_endpoint(
            "get_pi_cycle_top_indicator",
            self.cg.get_pi_cycle_top_indicator
        ))
        
        self.results.append(self.test_endpoint(
            "get_golden_ratio_multiplier",
            self.cg.get_golden_ratio_multiplier
        ))
        
        self.results.append(self.test_endpoint(
            "get_bitcoin_profitable_days",
            self.cg.get_bitcoin_profitable_days
        ))
        
        self.results.append(self.test_endpoint(
            "get_bitcoin_rainbow_chart",
            self.cg.get_bitcoin_rainbow_chart
        ))
    
    def run_all_tests(self):
        """Run all endpoint tests."""
        print("=" * 80)
        print("COINGLASS API COMPREHENSIVE ENDPOINT TEST")
        print("=" * 80)
        print(f"API Key: {self.api_key[:10]}...{self.api_key[-4:]}")
        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)
        
        # Test all categories
        self.test_all_futures_endpoints()
        self.test_all_spot_endpoints()
        self.test_all_option_endpoints()
        self.test_all_exchange_endpoints()
        self.test_all_etf_endpoints()
        self.test_all_grayscale_endpoints()
        self.test_all_hyperliquid_endpoints()
        self.test_all_index_endpoints()
        self.test_all_calendar_endpoints()
        self.test_all_toplevel_endpoints()
        
        # Print results table
        self.print_results()
        
        # Close connection
        self.cg.close()
    
    def print_results(self):
        """Print test results in formatted tables."""
        print("\n" + "=" * 80)
        print("TEST RESULTS")
        print("=" * 80)
        
        # Display each result as a small table
        for i, result_tuple in enumerate(self.results, 1):
            # Handle both old and new tuple formats
            if len(result_tuple) == 6:
                name, url, plan_required, params, status, result = result_tuple
            elif len(result_tuple) == 5:
                name, url, params, status, result = result_tuple
                plan_required = PlanTier.ALL
            else:
                name, params, status, result = result_tuple
                url = "N/A"
                plan_required = PlanTier.ALL
            print(f"\n### Test #{i}\n")
            print("| Field | Value |")
            print("|-------|-------|")
            print(f"| **Endpoint** | `{name}` |")
            print(f"| **URL** | `{url}` |")
            print(f"| **Plan Required** | {plan_required} |")
            
            # Format parameters - escape pipes and truncate if needed
            params_display = params.replace("|", "\\|") if params else "None"
            if len(params_display) > 100:
                params_display = params_display[:97] + "..."
            print(f"| **Parameters** | `{params_display}` |")
            
            # Status
            print(f"| **Status** | {status} |")
            
            # Format response - escape pipes and truncate if needed
            result_display = result.replace("|", "\\|").replace("\n", " ") if result else ""
            if len(result_display) > 150:
                result_display = result_display[:147] + "..."
            
            # For successful responses, format them better
            if "SUCCESS" in status:
                if result_display.startswith("List["):
                    # Extract list info
                    print(f"| **Response Type** | List |")
                    match = re.match(r"List\[(\d+)\]", result_display)
                    if match:
                        print(f"| **Item Count** | {match.group(1)} |")
                        # Show sample data if available
                        sample = result_display[len(match.group(0)):].strip(": ")
                        if sample and sample != "...":
                            print(f"| **Sample Data** | `{sample[:100]}...` |")
                elif result_display.startswith("{"):
                    print(f"| **Response Type** | Object |")
                    print(f"| **Data** | `{result_display[:100]}...` |")
                else:
                    print(f"| **Response** | `{result_display}` |")
            else:
                # For errors, show the error message
                print(f"| **Error** | `{result_display}` |")
            
            # Print a separator every 5 tests for readability
            if i % 5 == 0:
                print("\n---")
        
        # Calculate statistics
        total = len(self.results)
        successful = sum(1 for r in self.results if "SUCCESS" in (r[4] if len(r) == 6 else r[3] if len(r) == 5 else r[2]))
        failed = total - successful
        success_rate = (successful / total * 100) if total > 0 else 0
        
        print("\n" + "=" * 80)
        print("SUMMARY")
        print("=" * 80)
        
        print("\n| Metric | Value |")
        print("|--------|-------|")
        print(f"| **Total Endpoints Tested** | {total} |")
        print(f"| **Successful** | ✅ {successful} |")
        print(f"| **Failed** | ❌ {failed} |")
        print(f"| **Success Rate** | {success_rate:.1f}% |")
        print(f"| **Completed** | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} |")
        
        print("\n" + "=" * 80)
        
        # Save detailed results to file
        self.save_detailed_results()
    
    def save_detailed_results(self):
        """Save detailed results to a JSON file."""
        output_file = f"test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        detailed_results = {
            "test_run": {
                "timestamp": datetime.now().isoformat(),
                "api_key_partial": f"{self.api_key[:10]}...{self.api_key[-4:]}",
                "total_endpoints": len(self.results),
                "successful": sum(1 for r in self.results if "SUCCESS" in (r[4] if len(r) == 6 else r[3] if len(r) == 5 else r[2])),
                "failed": sum(1 for r in self.results if "FAILED" in (r[4] if len(r) == 6 else r[3] if len(r) == 5 else r[2]))
            },
            "endpoints": [
                {
                    "number": i,
                    "endpoint": r[0],
                    "url": r[1] if len(r) >= 5 else "N/A",
                    "plan_required": r[2] if len(r) == 6 else PlanTier.ALL,
                    "parameters": r[3] if len(r) == 6 else r[2] if len(r) == 5 else r[1],
                    "status": r[4] if len(r) == 6 else r[3] if len(r) == 5 else r[2],
                    "response": r[5] if len(r) == 6 else r[4] if len(r) == 5 else r[3]
                }
                for i, r in enumerate(self.results, 1)
            ]
        }
        
        with open(output_file, 'w') as f:
            json.dump(detailed_results, f, indent=2)
        
        print(f"\nDetailed results saved to: {output_file}")


def main():
    """Main function to run all tests."""
    try:
        tester = EndpointTester()
        tester.run_all_tests()
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()