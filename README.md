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
git clone https://github.com/yourusername/coinglass-python.git
cd coinglass-python
pip install -e .
```

### Development Installation
```bash
pip install -e ".[dev]"
```

## Quick Start

### Basic Usage

```python
from coinglass import CoinGlass

# Initialize the client with your API key
cg = CoinGlass(api_key="your_api_key_here")

# Or set CG_API_KEY environment variable
# export CG_API_KEY="your_api_key_here"
cg = CoinGlass()

# Get supported futures coins
coins = cg.futures.get_supported_coins()
print(f"Supported coins: {coins}")

# Get Bitcoin futures market data
btc_markets = cg.futures.get_coins_markets()
btc_data = [m for m in btc_markets if m['symbol'] == 'BTC'][0]
print(f"BTC Price: ${btc_data['current_price']:,.2f}")
print(f"24h Change: {btc_data['price_change_percent_24h']:.2f}%")
```

### Using Context Manager

```python
from coinglass import CoinGlass

with CoinGlass(api_key="your_api_key") as cg:
    # Get fear and greed index
    fear_greed = cg.index.get_fear_greed_history()
    print(f"Current Fear & Greed: {fear_greed[-1]['value']}")
```

## API Modules

### 📊 Futures Module

Access comprehensive futures market data:

```python
# Get futures market overview
markets = cg.futures.get_coins_markets()

# Get open interest data
oi_history = cg.futures.open_interest.get_history(
    symbol="BTCUSDT_PERP",
    interval="1h"
)

# Get funding rates
funding_rates = cg.futures.funding_rate.get_exchange_list(symbol="BTC")

# Get liquidation data
liquidations = cg.futures.liquidation.get_history(
    symbol="BTCUSDT",
    interval="1h"
)

# Get long/short ratios
ls_ratio = cg.futures.global_long_short_account_ratio.get_history(
    symbol="BTC",
    interval="1h"
)
```

### 💹 Spot Module

Access spot market data:

```python
# Get spot markets
spot_markets = cg.spot.get_pairs_markets()

# Get spot price history
price_history = cg.spot.price.get_history(
    symbol="BTC/USDT",
    interval="1h"
)

# Get order book data
orderbook = cg.spot.orderbook.get_large_limit_order(symbol="BTC/USDT")
```

### 🎯 Options Module

Access options market data:

```python
# Get max pain data
max_pain = cg.option.get_max_pain(symbol="BTC")

# Get options info
options_info = cg.option.get_info(symbol="BTC")

# Get options volume history
vol_history = cg.option.get_exchange_vol_history(
    symbol="BTC",
    unit="USD"
)
```

### 🔗 On-Chain Module

Access on-chain and exchange data:

```python
# Get exchange reserves
exchange_assets = cg.exchange.get_assets(exchange="Binance")

# Get on-chain balance
btc_balance = cg.exchange.balance.get_list(symbol="BTC")

# Get on-chain transactions
transactions = cg.exchange.chain.tx.get_list(
    exchange="Binance",
    symbol="USDT"
)
```

### 📈 ETF Module

Access ETF data:

```python
# Get Bitcoin ETF list
btc_etfs = cg.etf.bitcoin.get_list()

# Get ETF flows
etf_flows = cg.etf.bitcoin.get_flow_history()

# Get Ethereum ETF data
eth_etfs = cg.etf.ethereum.get_list()
```

### 📊 Indicators Module

Access various market indicators:

```python
# Fear and Greed Index
fear_greed = cg.index.get_fear_greed_history()

# Bitcoin indicators
ahr999 = cg.index.get_ahr999()
pi_cycle = cg.get_pi_cycle_top_indicator()
rainbow_chart = cg.get_bitcoin_rainbow_chart()

# On-chain metrics
active_addresses = cg.index.get_bitcoin_active_addresses()
nupl = cg.index.get_bitcoin_net_unrealized_pnl()

# Market structure
altcoin_season = cg.index.get_altcoin_season_index()
btc_correlations = cg.index.get_btc_correlations()
```

### 🐋 Hyperliquid Module

Access Hyperliquid DEX data:

```python
# Get whale alerts
whale_alerts = cg.hyperliquid.get_whale_alert()

# Get whale positions
whale_positions = cg.hyperliquid.get_whale_position()
```

### 📅 Calendar Module

Access economic calendar:

```python
# Get economic events
events = cg.calendar.get_economic_data()
```

## Complete Endpoint List

The library implements all 116 CoinGlass API endpoints:

### Futures (44 endpoints)
- Market data: coins/pairs markets, price changes
- Open Interest: history, aggregated, by exchange
- Funding Rates: history, weighted averages, arbitrage
- Liquidations: history, heatmaps, maps
- Order Book: depth, large orders
- Long/Short Ratios: global, top traders
- Volume: taker buy/sell
- Indicators: RSI, basis, whale index, CGDI, CDRI

### Spot (13 endpoints)
- Market data: coins/pairs markets
- Price history
- Order book data
- Volume analysis

### Options (4 endpoints)
- Max pain calculations
- Options info and metrics
- OI and volume history

### On-Chain (15 endpoints)
- Exchange reserves and balances
- ETF data (Bitcoin, Ethereum, HK)
- Grayscale holdings
- On-chain transfers

### Indicators (40 endpoints)
- Market indicators: Fear & Greed, correlations
- Bitcoin indicators: Pi Cycle, Rainbow Chart, Stock-to-Flow
- On-chain metrics: NUPL, SOPR, active addresses
- Market structure: altcoin season, M2 growth comparison

## Advanced Usage

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
    timeout=60,  # 60 second timeout
    max_retries=5  # Retry failed requests up to 5 times
)
```

### Error Handling

```python
from coinglass import CoinGlass, CoinGlassAPIError, CoinGlassRateLimitError

cg = CoinGlass(api_key="your_api_key")

try:
    data = cg.futures.get_coins_markets()
except CoinGlassRateLimitError as e:
    print(f"Rate limited. Retry after {e.retry_after} seconds")
except CoinGlassAPIError as e:
    print(f"API Error [{e.code}]: {e.message}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Async Support (Future)

The library is designed with async support in mind for future MCP server integration:

```python
# Future async implementation (not yet available)
import asyncio
from coinglass.async_client import AsyncCoinGlass

async def main():
    async with AsyncCoinGlass(api_key="your_api_key") as cg:
        markets = await cg.futures.get_coins_markets()
        print(markets)

asyncio.run(main())
```

## MCP Server Integration

This library is specifically designed for easy integration with MCP (Model Context Protocol) servers:

```python
# Example MCP server integration
from coinglass import CoinGlass
from mcp import Server, Tool

class CoinGlassMCPServer:
    def __init__(self, api_key: str):
        self.cg = CoinGlass(api_key=api_key)
        self.server = Server("coinglass-mcp")
        self.register_tools()
    
    def register_tools(self):
        @self.server.tool("get_btc_price")
        async def get_btc_price():
            """Get current Bitcoin price and market data"""
            markets = self.cg.futures.get_coins_markets()
            btc = next(m for m in markets if m['symbol'] == 'BTC')
            return {
                "price": btc['current_price'],
                "24h_change": btc['price_change_percent_24h'],
                "volume": btc['volume_usd']
            }
        
        @self.server.tool("get_liquidations")
        async def get_liquidations(symbol: str = "BTC"):
            """Get recent liquidation data"""
            return self.cg.futures.liquidation.get_history(
                symbol=symbol,
                interval="1h"
            )
```

## Environment Variables

The library supports the following environment variables:

```bash
# API Authentication
CG_API_KEY=your_api_key_here

# Optional: Override API base URL
CG_BASE_URL=https://open-api-v4.coinglass.com/api
```

## Rate Limiting

The CoinGlass API has rate limits based on your subscription plan:
- **Hobbyist**: Lower rate limits, some endpoints restricted
- **Startup**: Higher rate limits, 30m minimum intervals
- **Standard**: Full access with 4h minimum intervals for some endpoints
- **Professional**: Highest rate limits, full access

The library automatically handles rate limiting with exponential backoff and retry logic.

## Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=coinglass

# Run specific test file
pytest tests/test_futures.py

# Run with verbose output
pytest -v
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/coinglass-python.git
cd coinglass-python

# Install in development mode
pip install -e ".[dev]"

# Run code formatting
black coinglass/
isort coinglass/

# Run linting
flake8 coinglass/
mypy coinglass/

# Run tests
pytest
```

## API Documentation

For detailed API documentation, please refer to:
- [CoinGlass Official API Documentation](https://coinglass.com/api)
- [Library API Reference](docs/api_reference.md)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This is an unofficial Python library for the CoinGlass API. It is not affiliated with, maintained, authorized, endorsed, or sponsored by CoinGlass. Use at your own risk.

Trading cryptocurrencies carries a risk of financial loss. The developers of this library are not responsible for any financial losses incurred through the use of this library.

## Support

- 📧 Email: your-email@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/coinglass-python/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/yourusername/coinglass-python/discussions)

## Acknowledgments

- Thanks to CoinGlass for providing the comprehensive API
- Built with ❤️ for the crypto community

---

**Note**: Remember to keep your API key secure and never commit it to version control. Always use environment variables or secure configuration management for production deployments.