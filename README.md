# CoinGlass Python Library

A comprehensive Python library for interacting with the CoinGlass API v4, providing access to cryptocurrency futures, spot, options, on-chain data, and various market indicators.

## Features

- 🚀 **Complete API Coverage**: All 116 CoinGlass API endpoints implemented
- 📊 **Multiple Market Types**: Futures, Spot, Options, and On-chain data
- 📈 **Rich Indicators**: 20+ Bitcoin indicators and market metrics
- 🔐 **Secure**: API key authentication with secure header transmission
- ⚡ **Efficient**: Built-in rate limiting and retry logic
- 🧩 **MCP Ready**: Designed for easy integration with MCP servers
- 📝 **Type Hints**: Full type annotations for better IDE support
- 🛡️ **Error Handling**: Comprehensive error handling with custom exceptions

## Installation

### From PyPI (when published)
```bash
pip install coinglass
```

### From Source
```bash
git clone https://github.com/SnakeO/coinglass-python.git
cd coinglass-python
pip install -e .
```

### Development Installation
```bash
pip install -e ".[dev]"
```

## Quick Start

### Basic Setup

```python
from coinglass import CoinGlass

# Initialize with API key
cg = CoinGlass(api_key="your_api_key_here")

# Or use environment variable
# export CG_API_KEY="your_api_key_here"
cg = CoinGlass()
```

## Complete API Reference - All 116 Endpoints

### Futures Module (44 endpoints)

#### 1. Get Supported Coins
```python
coins = cg.futures.get_supported_coins()
# Output: ['BTC', 'ETH', 'SOL', 'XRP', 'DOGE', 'ADA', 'AVAX', ...]
```

#### 2. Get Supported Exchange Pairs
```python
pairs = cg.futures.get_supported_exchange_pairs()
# Output: {
#   'Binance': [
#     {'instrument_id': 'BTCUSD_PERP', 'base_asset': 'BTC', 'quote_asset': 'USD'},
#     {'instrument_id': 'BTCUSD_250627', 'base_asset': 'BTC', 'quote_asset': 'USD'},
#     ...
#   ],
#   'Bitget': [...],
#   ...
# }
```

#### 3. Get Coins Markets
```python
markets = cg.futures.get_coins_markets()
# Output: [
#   {
#     'symbol': 'BTC',
#     'current_price': 84773.6,
#     'avg_funding_rate_by_oi': 0.00196,
#     'avg_funding_rate_by_vol': 0.002647,
#     'market_cap_usd': 1683310500117.051,
#     'open_interest_market_cap_ratio': 0.0327,
#     'open_interest_usd': 55002072334.9376,
#     'open_interest_quantity': 648525.0328,
#     'open_interest_volume_ratio': 0.7936,
#     'price_change_percent_24h': 1.06,
#     'open_interest_change_percent_24h': 4.58,
#     'volume_change_percent_24h': -26.38,
#     'volume_change_usd_24h': -24835757605.82467,
#     'long_short_ratio_24h': 1.0313,
#     'liquidation_usd_24h': 27519292.973646,
#     'long_liquidation_usd_24h': 17793322.595016,
#     'short_liquidation_usd_24h': 9725970.37863
#   },
#   ...
# ]
```

#### 4. Get Pairs Markets
```python
pairs_markets = cg.futures.get_pairs_markets()
# Output: [
#   {
#     'instrument_id': 'BTCUSDT',
#     'exchange_name': 'Binance',
#     'symbol': 'BTC/USDT',
#     'current_price': 84604.3,
#     'index_price': 84646.6622,
#     'price_change_percent_24h': 0.67,
#     'volume_usd': 11317580109.5041,
#     'volume_usd_change_percent_24h': -32.13,
#     'long_volume_usd': 5800829746.047,
#     'short_volume_usd': 5516750363.4571,
#     'open_interest_quantity': 77881.234,
#     'open_interest_usd': 6589095073.8296,
#     'funding_rate': 0.002007,
#     'next_funding_time': 1744963200000
#   },
#   ...
# ]
```

#### 5. Get Coins Price Change
```python
price_changes = cg.futures.get_coins_price_change()
# Output: [
#   {
#     'symbol': 'BTC',
#     'current_price': 84518.4,
#     'price_change_percent_5m': -0.04,
#     'price_change_percent_15m': -0.09,
#     'price_change_percent_30m': -0.11,
#     'price_change_percent_1h': -0.17,
#     'price_change_percent_4h': -0.54,
#     'price_change_percent_12h': -0.6,
#     'price_change_percent_24h': 0.24,
#     'price_amplitude_percent_5m': 0.07,
#     'price_amplitude_percent_15m': 0.16,
#     'price_amplitude_percent_30m': 0.18,
#     'price_amplitude_percent_1h': 0.26,
#     'price_amplitude_percent_4h': 0.63,
#     'price_amplitude_percent_12h': 1.17,
#     'price_amplitude_percent_24h': 2.06
#   },
#   ...
# ]
```

#### 6. Get Price History
```python
price_history = cg.futures.price.get_history(symbol='BTC', interval='1h')
# Output: [
#   {
#     'time': 1745366400000,
#     'open': '93404.9',
#     'high': '93864.9',
#     'low': '92730',
#     'close': '92858.2',
#     'volume_usd': '1166471854.3026'
#   },
#   {
#     'time': 1745370000000,
#     'open': '92858.2',
#     'high': '93464.8',
#     'low': '92552',
#     'close': '92603.8',
#     'volume_usd': '871812560.3437'
#   },
#   ...
# ]
```

#### 7. Get Delisted Pairs
```python
delisted = cg.futures.get_delisted_pairs()
# Output: ['BINANCE_BTCUSD_200925', 'OKEX_ETHUSD_210326', 'HUOBI_LINKUSD_201225', ...]
```

#### 8. Get Exchange Rank
```python
exchange_rank = cg.futures.get_exchange_rank()
# Output: [
#   {
#     'exchange': 'Binance',
#     'open_interest_usd': 60000000000,
#     'volume_usd': 120000000000,
#     'market_share_percent': 35.2
#   },
#   {
#     'exchange': 'OKX',
#     'open_interest_usd': 25000000000,
#     'volume_usd': 80000000000,
#     'market_share_percent': 18.5
#   },
#   ...
# ]
```

#### 9. Get Open Interest History
```python
oi_history = cg.futures.open_interest.get_history(symbol='BTCUSDT_PERP', interval='4h')
# Output: [
#   {
#     'time': 1658880000000,
#     'open': '2644845344',
#     'high': '2692643311',
#     'low': '2576975597',
#     'close': '2608846475'
#   },
#   ...
# ]
```

#### 10. Get Aggregated Open Interest History
```python
agg_oi = cg.futures.open_interest.get_aggregated_history(symbol='BTC', interval='1d')
# Output: [
#   {
#     'time': 1658880000000,
#     'open': '52644845344',
#     'high': '53692643311',
#     'low': '51576975597',
#     'close': '52608846475'
#   },
#   ...
# ]
```

#### 11. Get Aggregated Stablecoin Margin History
```python
stablecoin_oi = cg.futures.open_interest.get_aggregated_stablecoin_margin_history(symbol='BTC', interval='4h')
# Output: Similar OHLC format for stablecoin-margined contracts
```

#### 12. Get Aggregated Coin Margin History
```python
coin_margin_oi = cg.futures.open_interest.get_aggregated_coin_margin_history(symbol='BTC', interval='4h')
# Output: Similar OHLC format for coin-margined contracts
```

#### 13. Get Open Interest by Exchange
```python
oi_by_exchange = cg.futures.open_interest.get_exchange_list(symbol='BTC')
# Output: {
#   'symbol': 'BTC',
#   'stablecoin_margin_list': [
#     {'exchange': 'Binance', 'open_interest': 30000000000},
#     {'exchange': 'Bybit', 'open_interest': 10000000000},
#     ...
#   ],
#   'coin_margin_list': [
#     {'exchange': 'Binance', 'open_interest': 5000},
#     {'exchange': 'OKX', 'open_interest': 8000},
#     ...
#   ]
# }
```

#### 14. Get Open Interest Exchange History Chart
```python
oi_chart = cg.futures.open_interest.get_exchange_history_chart(symbol='BTC')
# Output: {
#   'time_list': [1691460000000, 1691463600000, ...],
#   'price_list': [29140.9, 29245.1, ...],
#   'data_map': {
#     'huobi': [15167.03527, 15234.234, ...],
#     'gate': [23412.723, 23523.432, ...],
#     'binance': [450234.234, 452342.234, ...],
#     ...
#   }
# }
```

#### 15. Get Funding Rate History
```python
funding_history = cg.futures.funding_rate.get_history(symbol='BTCUSDT_PERP', interval='8h')
# Output: [
#   {'time': 1658880000000, 'open': '0.0001', 'high': '0.0003', 'low': '0.0001', 'close': '0.0002'},
#   ...
# ]
```

#### 16. Get OI-Weighted Funding Rate History
```python
oi_weighted_funding = cg.futures.funding_rate.get_oi_weight_history(symbol='BTC', interval='8h')
# Output: Similar OHLC format with OI-weighted funding rates
```

#### 17. Get Volume-Weighted Funding Rate History
```python
vol_weighted_funding = cg.futures.funding_rate.get_vol_weight_history(symbol='BTC', interval='8h')
# Output: Similar OHLC format with volume-weighted funding rates
```

#### 18. Get Funding Rate by Exchange
```python
funding_by_exchange = cg.futures.funding_rate.get_exchange_list(symbol='BTC')
# Output: [
#   {'exchange': 'Binance', 'funding_rate': 0.00125},
#   {'exchange': 'OKX', 'funding_rate': 0.00110},
#   {'exchange': 'Bybit', 'funding_rate': 0.00135},
#   ...
# ]
```

#### 19. Get Accumulated Funding Rate by Exchange
```python
accumulated_funding = cg.futures.funding_rate.get_accumulated_exchange_list(symbol='BTC')
# Output: [
#   {'exchange': 'Binance', 'cumulative_funding_rate': 1.2345},
#   {'exchange': 'Bybit', 'cumulative_funding_rate': 0.9876},
#   ...
# ]
```

#### 20. Get Funding Rate Arbitrage
```python
funding_arb = cg.futures.funding_rate.get_arbitrage(symbol='BTC')
# Output: [
#   {'exchange_pair': 'Binance_vs_OKX', 'rate_diff': 0.00015},
#   {'exchange_pair': 'Binance_vs_Bybit', 'rate_diff': -0.0001},
#   ...
# ]
```

#### 21. Get Global Long/Short Account Ratio History
```python
global_ls = cg.futures.global_long_short_account_ratio.get_history(symbol='BTC', interval='1h')
# Output: [
#   {'time': 1658880000000, 'long_account': 0.52, 'short_account': 0.48, 'ratio': 1.0833},
#   ...
# ]
```

#### 22. Get Top Long/Short Account Ratio History
```python
top_ls_account = cg.futures.top_long_short_account_ratio.get_history(symbol='BTC', interval='1h')
# Output: [
#   {'time': 1658880000000, 'long_account': 0.55, 'short_account': 0.45, 'ratio': 1.222},
#   ...
# ]
```

#### 23. Get Top Long/Short Position Ratio History
```python
top_ls_position = cg.futures.top_long_short_position_ratio.get_history(symbol='BTC', interval='1h')
# Output: [
#   {'time': 1658880000000, 'long_position': 0.58, 'short_position': 0.42, 'ratio': 1.381},
#   ...
# ]
```

#### 24. Get Taker Buy/Sell Volume by Exchange
```python
taker_vol_exchange = cg.futures.taker_buy_sell_volume.get_exchange_list(symbol='BTC')
# Output: [
#   {'exchange': 'Binance', 'buy_sell_ratio': 1.12},
#   {'exchange': 'OKX', 'buy_sell_ratio': 0.98},
#   ...
# ]
```

#### 25. Get Liquidation History
```python
liq_history = cg.futures.liquidation.get_history(symbol='BTCUSDT', interval='1h')
# Output: [
#   {
#     'time': 1658880000000,
#     'long_liquidation_usd': '2369935.19562',
#     'short_liquidation_usd': '6947459.43674'
#   },
#   {
#     'time': 1658966400000,
#     'long_liquidation_usd': '5118407.85124',
#     'short_liquidation_usd': '8517330.44192'
#   },
#   ...
# ]
```

#### 26. Get Aggregated Liquidation History
```python
agg_liq = cg.futures.liquidation.get_aggregated_history(symbol='BTC', interval='1h')
# Output: [
#   {
#     'time': 1658880000000,
#     'long_liquidation_usd': '23699351.19562',
#     'short_liquidation_usd': '69474594.43674'
#   },
#   ...
# ]
```

#### 27. Get Liquidation Coin List
```python
liq_coins = cg.futures.liquidation.get_coin_list()
# Output: ['BTC', 'ETH', 'XRP', 'SOL', 'DOGE', 'ADA', ...]
```

#### 28. Get Liquidation Exchange List
```python
liq_exchanges = cg.futures.liquidation.get_exchange_list()
# Output: ['Binance', 'OKX', 'Bybit', 'Coinbase', 'Kraken', ...]
```

#### 29. Get Large Liquidation Orders
```python
large_liqs = cg.futures.liquidation.get_order()
# Output: [
#   {
#     'timestamp': 1695043200000,
#     'exchange': 'Binance',
#     'symbol': 'BTCUSDT',
#     'side': 'long',
#     'quantity': 1500000,
#     'price': 82000
#   },
#   ...
# ]
```

#### 30-32. Get Liquidation Heatmap (Models 1-3)
```python
# Model 1
heatmap1 = cg.futures.liquidation.heatmap.get_model1(symbol='BTCUSDT')
# Model 2
heatmap2 = cg.futures.liquidation.heatmap.get_model2(symbol='BTCUSDT')
# Model 3
heatmap3 = cg.futures.liquidation.heatmap.get_model3(symbol='BTCUSDT')
# Output: Complex heatmap data structure with price levels and liquidation clusters
```

#### 33-35. Get Aggregated Liquidation Heatmap (Models 1-3)
```python
# Model 1
agg_heatmap1 = cg.futures.liquidation.aggregated_heatmap.get_model1(symbol='BTC')
# Model 2
agg_heatmap2 = cg.futures.liquidation.aggregated_heatmap.get_model2(symbol='BTC')
# Model 3
agg_heatmap3 = cg.futures.liquidation.aggregated_heatmap.get_model3(symbol='BTC')
# Output: Complex aggregated heatmap data across all exchanges
```

#### 36. Get Liquidation Map
```python
liq_map = cg.futures.liquidation.get_map(symbol='BTCUSDT')
# Output: Liquidation clusters and levels for visualization
```

#### 37. Get Aggregated Liquidation Map
```python
agg_liq_map = cg.futures.liquidation.get_aggregated_map(symbol='BTC')
# Output: Aggregated liquidation clusters across all exchanges
```

#### 38. Get Order Book Ask/Bids History
```python
orderbook_history = cg.futures.orderbook.get_ask_bids_history(symbol='BTCUSDT', interval='1h', range=0.01)
# Output: [
#   {
#     'time': 1658880000000,
#     'bid_volume': 234523.34,
#     'ask_volume': 198234.23,
#     'bid_ask_ratio': 1.183
#   },
#   ...
# ]
```

#### 39. Get Aggregated Order Book Ask/Bids History
```python
agg_orderbook = cg.futures.orderbook.get_aggregated_ask_bids_history(symbol='BTC', interval='1h', range=0.01)
# Output: Similar format but aggregated across exchanges
```

#### 40. Get Order Book History
```python
orderbook_heatmap = cg.futures.orderbook.get_history(symbol='BTCUSDT', interval='1h')
# Output: Order book depth distribution over time
```

#### 41. Get Large Limit Orders
```python
large_orders = cg.futures.orderbook.get_large_limit_order(symbol='BTCUSDT')
# Output: [
#   {'price': 84000, 'quantity': 500, 'side': 'buy', 'exchange': 'Binance'},
#   {'price': 85000, 'quantity': 300, 'side': 'sell', 'exchange': 'Binance'},
#   ...
# ]
```

#### 42. Get Large Limit Order History
```python
large_order_history = cg.futures.orderbook.get_large_limit_order_history(symbol='BTCUSDT', interval='1h')
# Output: Historical data of large orders
```

#### 43. Get Taker Buy/Sell Volume History
```python
taker_vol = cg.futures.taker_buy_sell_volume.get_history(symbol='BTCUSDT', interval='1h')
# Output: [
#   {'time': 1658880000000, 'buy_volume': 5234234.23, 'sell_volume': 4923432.12},
#   ...
# ]
```

#### 44. Get Aggregated Taker Buy/Sell Volume History
```python
agg_taker_vol = cg.futures.aggregated_taker_buy_sell_volume.get_history(symbol='BTC', interval='1h')
# Output: [
#   {'time': 1658880000000, 'buy_volume': 52342342.23, 'sell_volume': 49234321.12},
#   ...
# ]
```

#### 45. Get RSI List
```python
rsi_data = cg.futures.rsi.get_list()
# Output: [
#   {'symbol': 'BTC', 'rsi_1h': 65.23, 'rsi_4h': 58.12, 'rsi_1d': 52.34},
#   {'symbol': 'ETH', 'rsi_1h': 70.45, 'rsi_4h': 62.23, 'rsi_1d': 55.67},
#   ...
# ]
```

#### 46. Get Basis
```python
basis = cg.futures.get_basis(symbol='BTC')
# Output: {
#   'spot_price': 84000,
#   'futures_price': 84150,
#   'basis': 150,
#   'basis_percent': 0.1786
# }
```

#### 47. Get Whale Index
```python
whale_index = cg.futures.get_whale_index()
# Output: {'index_value': 0.73, 'sentiment': 'bullish', 'timestamp': 1695043200000}
```

#### 48. Get CGDI Index
```python
cgdi = cg.futures.get_cgdi_index()
# Output: {'index_value': 0.65, 'description': 'CoinGlass Derivatives Index', 'timestamp': 1695043200000}
```

#### 49. Get CDRI Index
```python
cdri = cg.futures.get_cdri_index()
# Output: {'index_value': 0.42, 'description': 'CoinGlass Derivatives Risk Index', 'timestamp': 1695043200000}
```

### Hyperliquid Module (2 endpoints)

#### 50. Get Whale Alert
```python
whale_alerts = cg.hyperliquid.get_whale_alert()
# Output: [
#   {
#     'timestamp': 1696050000000,
#     'symbol': 'ETHUSDT',
#     'action': 'large_trade',
#     'details': {'side': 'buy', 'quantity': 5000, 'price': 1600}
#   },
#   ...
# ]
```

#### 51. Get Whale Position
```python
whale_positions = cg.hyperliquid.get_whale_position()
# Output: [
#   {
#     'wallet': '0xABC123...',
#     'position_value_usd': 10000000,
#     'asset': 'BTC',
#     'entry_price': 80000,
#     'unrealized_pnl_usd': -200000
#   },
#   ...
# ]
```

### Spot Module (13 endpoints)

#### 52. Get Spot Supported Coins
```python
spot_coins = cg.spot.get_supported_coins()
# Output: ['BTC', 'ETH', 'USDT', 'BNB', 'SOL', 'XRP', ...]
```

#### 53. Get Spot Supported Exchange Pairs
```python
spot_pairs = cg.spot.get_supported_exchange_pairs()
# Output: {
#   'Binance': [
#     {'symbol': 'BTC/USDT', 'base': 'BTC', 'quote': 'USDT'},
#     {'symbol': 'ETH/USDT', 'base': 'ETH', 'quote': 'USDT'},
#     ...
#   ],
#   ...
# }
```

#### 54. Get Spot Coins Markets
```python
spot_markets = cg.spot.get_coins_markets()
# Output: [
#   {
#     'symbol': 'BTC',
#     'current_price': 84500,
#     'price_change_percent_24h': 1.23,
#     'volume_usd': 35000000000,
#     'market_cap': 1650000000000
#   },
#   ...
# ]
```

#### 55. Get Spot Pairs Markets
```python
spot_pairs_markets = cg.spot.get_pairs_markets()
# Output: [
#   {
#     'symbol': 'BTC/USDT',
#     'exchange': 'Binance',
#     'current_price': 84500,
#     'volume_usd': 5000000000,
#     'bid': 84499,
#     'ask': 84501
#   },
#   ...
# ]
```

#### 56. Get Spot Price History
```python
spot_price_history = cg.spot.price.get_history(symbol='BTC/USDT', interval='1h')
# Output: [
#   {
#     'time': 1658880000000,
#     'open': '84000',
#     'high': '84500',
#     'low': '83800',
#     'close': '84300',
#     'volume': '523423.23'
#   },
#   ...
# ]
```

#### 57. Get Spot Order Book Ask/Bids History
```python
spot_orderbook = cg.spot.orderbook.get_ask_bids_history(symbol='BTC/USDT', interval='1h', range=0.01)
# Output: [
#   {'time': 1658880000000, 'bid_volume': 123.45, 'ask_volume': 98.23},
#   ...
# ]
```

#### 58. Get Spot Aggregated Order Book History
```python
spot_agg_orderbook = cg.spot.orderbook.get_aggregated_ask_bids_history(symbol='BTC', interval='1h', range=0.01)
# Output: Similar format but aggregated across exchanges
```

#### 59. Get Spot Order Book History
```python
spot_orderbook_history = cg.spot.orderbook.get_history(symbol='BTC/USDT', interval='1h')
# Output: Order book depth over time
```

#### 60. Get Spot Large Limit Orders
```python
spot_large_orders = cg.spot.orderbook.get_large_limit_order(symbol='BTC/USDT')
# Output: [
#   {'price': 84000, 'quantity': 10, 'side': 'buy', 'exchange': 'Binance'},
#   ...
# ]
```

#### 61. Get Spot Large Limit Order History
```python
spot_large_order_history = cg.spot.orderbook.get_large_limit_order_history(symbol='BTC/USDT', interval='1h')
# Output: Historical large order data
```

#### 62. Get Spot Taker Buy/Sell Volume History
```python
spot_taker_vol = cg.spot.taker_buy_sell_volume.get_history(symbol='BTC/USDT', interval='1h')
# Output: [
#   {'time': 1658880000000, 'buy_volume': 234.56, 'sell_volume': 198.23},
#   ...
# ]
```

#### 63. Get Spot Aggregated Taker Buy/Sell Volume History
```python
spot_agg_taker_vol = cg.spot.aggregated_taker_buy_sell_volume.get_history(symbol='BTC', interval='1h')
# Output: [
#   {'time': 1658880000000, 'buy_volume': 2345.67, 'sell_volume': 1982.34},
#   ...
# ]
```

### Options Module (4 endpoints)

#### 64. Get Max Pain
```python
max_pain = cg.option.get_max_pain(symbol='BTC')
# Output: [
#   {
#     'date': '250422',
#     'call_open_interest': 953.7,
#     'put_open_interest': 512.5,
#     'call_open_interest_market_value': 1616749.22,
#     'put_open_interest_market_value': 49687.62,
#     'max_pain_price': '84000',
#     'call_open_interest_notional': 83519113.56,
#     'put_open_interest_notional': 44881569.13
#   },
#   ...
# ]
```

#### 65. Get Options Info
```python
options_info = cg.option.get_info(symbol='BTC')
# Output: {
#   'symbol': 'BTC',
#   'total_open_interest_usd': 500000000,
#   'total_volume_24h_usd': 80000000,
#   'put_call_ratio_oi': 0.85,
#   'put_call_ratio_vol': 0.9,
#   'implied_volatility': 0.65
# }
```

#### 66. Get Options Exchange OI History
```python
options_oi = cg.option.get_exchange_oi_history(symbol='BTC', unit='USD', range='1h')
# Output: [
#   {'time': 1658880000000, 'deribit': 350000000, 'okx': 120000000, 'binance': 30000000},
#   ...
# ]
```

#### 67. Get Options Exchange Volume History
```python
options_vol = cg.option.get_exchange_vol_history(symbol='BTC', unit='USD', range='1h')
# Output: [
#   {'time': 1658880000000, 'deribit': 50000000, 'okx': 20000000, 'binance': 10000000},
#   ...
# ]
```

### Exchange/On-Chain Module (4 endpoints)

#### 68. Get Exchange Assets
```python
exchange_assets = cg.exchange.get_assets(exchange='Binance')
# Output: [
#   {
#     'symbol': 'BTC',
#     'assets_name': 'Bitcoin',
#     'price': 87000.0,
#     'reserve_quantity': 50000.123,
#     'reserve_usd': 4350000000.0
#   },
#   {
#     'symbol': 'ETH',
#     'assets_name': 'Ethereum',
#     'price': 1600.5,
#     'reserve_quantity': 300000,
#     'reserve_usd': 480000000.0
#   },
#   ...
# ]
```

#### 69. Get Balance List
```python
balance_list = cg.exchange.balance.get_list(symbol='BTC')
# Output: [
#   {'exchange': 'Binance', 'reserve': 600000, 'unit': 'BTC'},
#   {'exchange': 'Coinbase', 'reserve': 300000, 'unit': 'BTC'},
#   {'exchange': 'Kraken', 'reserve': 150000, 'unit': 'BTC'},
#   ...
# ]
```

#### 70. Get Balance Chart
```python
balance_chart = cg.exchange.balance.get_chart(symbol='BTC')
# Output: {
#   'time_list': [1691460000000, 1691463600000, ...],
#   'price_list': [29140.9, 29245.1, ...],
#   'data_map': {
#     'Binance': [151670, 151234, ...],
#     'Coinbase': [234120, 233890, ...],
#     'Kraken': [98234, 98123, ...],
#     ...
#   }
# }
```

#### 71. Get Chain Transaction List
```python
chain_tx = cg.exchange.chain.tx.get_list(exchange='Binance', symbol='USDT')
# Output: [
#   {
#     'tx_time': 1696050000000,
#     'token': 'USDT',
#     'amount': 50000000,
#     'direction': 'inflow',
#     'tx_hash': '0x123abc...'
#   },
#   {
#     'tx_time': 1696053600000,
#     'token': 'USDT',
#     'amount': 30000000,
#     'direction': 'outflow',
#     'tx_hash': '0x456def...'
#   },
#   ...
# ]
```

### ETF Module (11 endpoints)

#### 72. Get Bitcoin ETF List
```python
btc_etf_list = cg.etf.bitcoin.get_list()
# Output: [
#   {'ticker': 'BITO', 'name': 'ProShares Bitcoin Strategy ETF'},
#   {'ticker': 'XBTF', 'name': 'VanEck Bitcoin Strategy ETF'},
#   {'ticker': 'GBTC', 'name': 'Grayscale Bitcoin Trust'},
#   ...
# ]
```

#### 73. Get Bitcoin ETF Net Assets History
```python
btc_etf_assets = cg.etf.bitcoin.net_assets.get_history()
# Output: [
#   {'date': '2024-01-01', 'total_net_assets': 25000000000, 'etf_breakdown': {...}},
#   ...
# ]
```

#### 74. Get Bitcoin ETF Flow History
```python
btc_etf_flows = cg.etf.bitcoin.get_flow_history()
# Output: [
#   {'date': '2024-01-01', 'net_flow': 500000000, 'inflow': 800000000, 'outflow': 300000000},
#   ...
# ]
```

#### 75. Get Bitcoin ETF Premium/Discount History
```python
btc_etf_premium = cg.etf.bitcoin.premium_discount.get_history()
# Output: [
#   {'date': '2024-01-01', 'gbtc_premium': -0.15, 'bito_premium': 0.02},
#   ...
# ]
```

#### 76. Get Bitcoin ETF History
```python
btc_etf_history = cg.etf.bitcoin.get_history()
# Output: Comprehensive ETF metrics over time
```

#### 77. Get Bitcoin ETF Price History
```python
btc_etf_price = cg.etf.bitcoin.price.get_history()
# Output: [
#   {'date': '2024-01-01', 'gbtc': 35.23, 'bito': 18.45, 'xbtf': 42.12},
#   ...
# ]
```

#### 78. Get Bitcoin ETF Detail
```python
btc_etf_detail = cg.etf.bitcoin.get_detail()
# Output: {
#   'gbtc': {'holdings': 650000, 'aum': 25000000000, 'expense_ratio': 0.02},
#   'bito': {'holdings': 0, 'aum': 1500000000, 'expense_ratio': 0.0095},
#   ...
# }
```

#### 79. Get Bitcoin ETF AUM
```python
btc_etf_aum = cg.etf.bitcoin.get_aum()
# Output: {
#   'total_aum': 35000000000,
#   'by_etf': {
#     'gbtc': 25000000000,
#     'bito': 1500000000,
#     ...
#   }
# }
```

#### 80. Get Ethereum ETF List
```python
eth_etf_list = cg.etf.ethereum.get_list()
# Output: [
#   {'ticker': 'ETHE', 'name': 'Grayscale Ethereum Trust'},
#   {'ticker': 'ETHW', 'name': 'WisdomTree Ethereum Fund'},
#   ...
# ]
```

#### 81. Get Ethereum ETF Net Assets History
```python
eth_etf_assets = cg.etf.ethereum.net_assets.get_history()
# Output: Similar to Bitcoin ETF net assets
```

#### 82. Get Ethereum ETF Flow History
```python
eth_etf_flows = cg.etf.ethereum.get_flow_history()
# Output: Similar to Bitcoin ETF flows
```

### Hong Kong ETF Module (1 endpoint)

#### 83. Get HK Bitcoin ETF Flow History
```python
hk_btc_flows = cg.hk_etf.bitcoin.get_flow_history()
# Output: [
#   {'date': '2024-01-01', 'net_flow': 50000000, 'inflow': 80000000, 'outflow': 30000000},
#   ...
# ]
```

### Grayscale Module (2 endpoints)

#### 84. Get Grayscale Holdings List
```python
grayscale_holdings = cg.grayscale.holdings.get_list()
# Output: [
#   {'trust': 'GBTC', 'asset': 'BTC', 'holdings': 650000},
#   {'trust': 'ETHE', 'asset': 'ETH', 'holdings': 3000000},
#   {'trust': 'LTCN', 'asset': 'LTC', 'holdings': 1500000},
#   ...
# ]
```

#### 85. Get Grayscale Premium History
```python
grayscale_premium = cg.grayscale.premium.get_history(symbol='GBTC')
# Output: [
#   {'date': '2024-01-01', 'premium': -0.15, 'nav': 35.50, 'market_price': 30.18},
#   ...
# ]
```

### Index/Indicators Module (20 endpoints)

#### 86. Get Fear & Greed History
```python
fear_greed = cg.index.get_fear_greed_history()
# Output: [
#   {'time': 1696118400000, 'value': 45, 'classification': 'Fear'},
#   {'time': 1696204800000, 'value': 50, 'classification': 'Neutral'},
#   {'time': 1696291200000, 'value': 75, 'classification': 'Greed'},
#   ...
# ]
```

#### 87. Get Option vs Futures OI Ratio
```python
option_futures_ratio = cg.index.get_option_vs_futures_oi_ratio()
# Output: [
#   {
#     'timestamp': 1592956800000,
#     'btc_option_vs_futures_ratio': 45.1,
#     'eth_option_vs_futures_ratio': 21.92
#   },
#   ...
# ]
```

#### 88. Get Bitcoin vs Global M2 Growth
```python
btc_vs_global_m2 = cg.index.get_bitcoin_vs_global_m2_growth()
# Output: [
#   {'date': '2024-01-01', 'btc_market_cap': 850000000000, 'global_m2': 105000000000000, 'ratio': 0.0081},
#   ...
# ]
```

#### 89. Get Bitcoin vs US M2 Growth
```python
btc_vs_us_m2 = cg.index.get_bitcoin_vs_us_m2_growth()
# Output: [
#   {'date': '2024-01-01', 'btc_market_cap': 850000000000, 'us_m2': 21000000000000, 'ratio': 0.0405},
#   ...
# ]
```

#### 90. Get Index AHR999
```python
index_ahr999 = cg.index.get_ahr999()
# Output: {'value': 0.45, 'status': 'undervalued', 'description': 'Good time to accumulate'}
```

#### 91. Get 2-Year MA Multiplier
```python
two_year_ma = cg.index.get_two_year_ma_multiplier()
# Output: {
#   'current_price': 84000,
#   '2_year_ma': 45000,
#   'multiplier': 1.87,
#   'status': 'neutral'
# }
```

#### 92. Get 200-Week Moving Avg Heatmap
```python
ma_200w_heatmap = cg.index.get_two_hundred_week_moving_avg_heatmap()
# Output: {
#   'current_price': 84000,
#   '200_week_ma': 35000,
#   'deviation': 140,
#   'heatmap_value': 0.7
# }
```

#### 93. Get Altcoin Season Index
```python
altcoin_season = cg.index.get_altcoin_season_index()
# Output: {
#   'index_value': 35,
#   'season': 'Bitcoin Season',
#   'description': '35% of top 50 coins outperformed Bitcoin over the last 90 days'
# }
```

#### 94. Get Bitcoin Short-Term Holder SOPR
```python
sth_sopr = cg.index.get_bitcoin_short_term_holder_sopr()
# Output: {'value': 1.02, 'status': 'profit', 'description': 'Short-term holders in profit'}
```

#### 95. Get Bitcoin Long-Term Holder SOPR
```python
lth_sopr = cg.index.get_bitcoin_long_term_holder_sopr()
# Output: {'value': 3.5, 'status': 'strong_profit', 'description': 'Long-term holders in strong profit'}
```

#### 96. Get Bitcoin Short-Term Holder Realized Price
```python
sth_realized_price = cg.index.get_bitcoin_short_term_holder_realized_price()
# Output: {'realized_price': 78000, 'current_price': 84000, 'premium': 0.077}
```

#### 97. Get Bitcoin Long-Term Holder Realized Price
```python
lth_realized_price = cg.index.get_bitcoin_long_term_holder_realized_price()
# Output: {'realized_price': 23000, 'current_price': 84000, 'premium': 2.65}
```

#### 98. Get Bitcoin Short-Term Holder Supply
```python
sth_supply = cg.index.get_bitcoin_short_term_holder_supply()
# Output: {'supply': 2500000, 'percentage': 0.119, 'change_30d': -50000}
```

#### 99. Get Bitcoin Long-Term Holder Supply
```python
lth_supply = cg.index.get_bitcoin_long_term_holder_supply()
# Output: {'supply': 15000000, 'percentage': 0.714, 'change_30d': 100000}
```

#### 100. Get Bitcoin RHODL Ratio
```python
rhodl = cg.index.get_bitcoin_rhodl_ratio()
# Output: {'value': 8500, 'status': 'neutral', 'description': 'Market neither overbought nor oversold'}
```

#### 101. Get Bitcoin Reserve Risk
```python
reserve_risk = cg.index.get_bitcoin_reserve_risk()
# Output: {'value': 0.003, 'status': 'low_risk', 'description': 'Good risk/reward for accumulation'}
```

#### 102. Get Bitcoin Active Addresses
```python
active_addresses = cg.index.get_bitcoin_active_addresses()
# Output: [
#   {'date': '2024-01-01', 'active_addresses': 950000, '7d_ma': 920000},
#   ...
# ]
```

#### 103. Get Bitcoin New Addresses
```python
new_addresses = cg.index.get_bitcoin_new_addresses()
# Output: [
#   {'date': '2024-01-01', 'new_addresses': 450000, '7d_ma': 430000},
#   ...
# ]
```

#### 104. Get Bitcoin Net Unrealized P&L
```python
nupl = cg.index.get_bitcoin_net_unrealized_pnl()
# Output: {'value': 0.65, 'status': 'belief', 'description': 'Market in belief phase'}
```

#### 105. Get BTC Correlations
```python
btc_correlations = cg.index.get_btc_correlations()
# Output: {
#   'sp500': 0.45,
#   'gold': 0.12,
#   'dxy': -0.35,
#   'nasdaq': 0.52,
#   'oil': 0.08
# }
```

#### 106. Get Bitcoin Macro Oscillator
```python
macro_oscillator = cg.index.get_bitcoin_macro_oscillator()
# Output: {'value': 0.7, 'status': 'risk_on', 'description': 'Favorable macro environment'}
```

### Calendar Module (1 endpoint)

#### 107. Get Economic Data
```python
economic_calendar = cg.calendar.get_economic_data()
# Output: [
#   {
#     'date': '2025-09-30',
#     'time': '08:30',
#     'event': 'US Nonfarm Payrolls',
#     'forecast': 250000,
#     'previous': 300000,
#     'impact': 'high'
#   },
#   {
#     'date': '2025-09-30',
#     'time': '09:00',
#     'event': 'EU CPI YoY',
#     'forecast': '2.1%',
#     'previous': '2.3%',
#     'impact': 'medium'
#   },
#   ...
# ]
```

### Top-Level Indicator Endpoints (11 endpoints)

#### 108. Get Coinbase Premium Index
```python
coinbase_premium = cg.get_coinbase_premium_index(interval='5m')
# Output: [
#   {'time': 1696000000000, 'premium_percent': 0.25},
#   {'time': 1696003600000, 'premium_percent': 0.30},
#   ...
# ]
```

#### 109. Get Bitfinex Margin Long/Short
```python
bitfinex_margin = cg.get_bitfinex_margin_long_short()
# Output: [
#   {
#     'time': 1658880000,
#     'long_quantity': 104637.94,
#     'short_quantity': 2828.53,
#     'ratio': 37.01
#   },
#   ...
# ]
```

#### 110. Get Borrow Interest Rate History
```python
borrow_rates = cg.get_borrow_interest_rate_history()
# Output: [
#   {'date': '2024-01-01', 'btc_rate': 0.0002, 'eth_rate': 0.0003, 'usdt_rate': 0.0008},
#   ...
# ]
```

#### 111. Get AHR999
```python
ahr999 = cg.get_ahr999()
# Output: {'value': 0.45, 'status': 'undervalued', 'description': 'Good accumulation zone'}
```

#### 112. Get Bull Market Peak Indicator
```python
peak_indicator = cg.get_bull_market_peak_indicator()
# Output: {
#   'thermocap_ratio': 0.0000045,
#   'pi_cycle_top': 85000,
#   'solow_value': 90000,
#   'mvrv': 2.3,
#   'puell_multiple': 1.2
# }
```

#### 113. Get Puell Multiple
```python
puell = cg.get_puell_multiple()
# Output: {'puell_multiple': 1.5, 'status': 'neutral', 'description': 'Mining profitability normal'}
```

#### 114. Get Stock-to-Flow
```python
s2f = cg.get_stock_to_flow()
# Output: {'s2f_value': 100000, 'model_price': 95000, 'actual_price': 84000, 'deviation': -11.6}
```

#### 115. Get Pi Cycle Top Indicator
```python
pi_cycle = cg.get_pi_cycle_top_indicator()
# Output: {'indicator': 85000, 'status': 'not_crossed', 'current_price': 84000}
```

#### 116. Get Golden Ratio Multiplier
```python
golden_ratio = cg.get_golden_ratio_multiplier()
# Output: {
#   'current_price': 84000,
#   'ma_350': 45000,
#   'multiplier': 1.87,
#   'fibonacci_levels': {
#     '1.6': 72000,
#     '2.0': 90000,
#     '3.0': 135000
#   }
# }
```


## Advanced Usage

### Error Handling

```python
from coinglass import CoinGlass, CoinGlassAPIError, CoinGlassRateLimitError

try:
    cg = CoinGlass(api_key="your_api_key")
    data = cg.futures.get_coins_markets()
except CoinGlassRateLimitError as e:
    print(f"Rate limited. Retry after {e.retry_after} seconds")
except CoinGlassAPIError as e:
    print(f"API Error [{e.code}]: {e.message}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Using with Context Manager

```python
with CoinGlass(api_key="your_api_key") as cg:
    # API calls here
    markets = cg.futures.get_coins_markets()
    # Connection automatically closed on exit
```

### Custom Session Configuration

```python
import requests
from coinglass import CoinGlass

# Create custom session with proxy
session = requests.Session()
session.proxies = {
    'http': 'http://proxy.example.com:8080',
    'https': 'https://proxy.example.com:8080'
}

cg = CoinGlass(
    api_key="your_api_key",
    session=session,
    timeout=60,
    max_retries=5
)
```

## MCP Server Integration

This library is designed for easy integration with MCP (Model Context Protocol) servers. See `examples/mcp_server_example.py` for a complete implementation.

## Rate Limiting

The CoinGlass API has rate limits based on your subscription plan:
- **Hobbyist**: Basic rate limits
- **Startup**: Higher limits, 30m minimum intervals
- **Standard**: Full access, 4h minimum for some endpoints
- **Professional**: Highest limits

The library automatically handles rate limiting with exponential backoff.

## Environment Variables

```bash
# API Authentication
export CG_API_KEY=your_api_key_here

# Optional: Override base URL
export CG_BASE_URL=https://open-api-v4.coinglass.com/api
```

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=coinglass

# Run specific test file
pytest tests/test_futures.py
```

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add tests for new features
4. Submit a pull request

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Disclaimer

This is an unofficial Python library for the CoinGlass API. Use at your own risk. Trading cryptocurrencies carries financial risk.

## Support

- 📧 Issues: [GitHub Issues](https://github.com/SnakeO/coinglass-python/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/SnakeO/coinglass-python/discussions)

---

**Note**: Always keep your API key secure. Never commit it to version control.