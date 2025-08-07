# CoinGlass API Plan Levels

## Overview

The CoinGlass API uses a numeric plan level system (1-5) to control access to endpoints. Each plan level provides access to more endpoints and features.

## Plan Level Mapping

| Level | Plan Name      | Description |
|-------|----------------|-------------|
| 1     | Hobbyist       | Basic access to most common endpoints |
| 2     | Startup        | Additional features for growing projects |
| 3     | Standard       | Professional features and advanced data |
| 4     | Professional   | Full access including liquidation maps |
| 5     | Enterprise     | Complete access to all endpoints |

## Configuration

### Environment Variable

Set your plan level in the `.env` file:

```bash
# Plan Level Configuration (1-5)
PLAN_LEVEL=3  # For Standard plan
```

### Programmatic Configuration

```python
from coinglass import CoinGlass

# Specify plan level directly
cg = CoinGlass(api_key="your_key", plan_level=3)

# Or it will use PLAN_LEVEL environment variable
cg = CoinGlass(api_key="your_key")
```

## Checking Endpoint Access

### Get Available Endpoints

```python
from coinglass import CoinGlass

cg = CoinGlass(api_key="your_key", plan_level=2)

# Get all endpoints available for your plan
available = cg.get_available_endpoints()
print(f"You have access to {len(available)} endpoints")

# Check a specific endpoint
if cg.check_endpoint_access("futures.liquidation.get_map"):
    print("You can access liquidation maps")
else:
    print("Liquidation maps require a higher plan")

# Get your current plan info
print(f"Current plan: Level {cg.get_plan_level()} ({cg.get_plan_name()})")

# Get statistics
stats = cg.get_endpoint_statistics()
print(f"Available: {stats['available_endpoints_count']} of {stats['total_endpoints']} endpoints")
```

### Using the Endpoint Registry

```python
from coinglass.endpoints import EndpointRegistry

# Get all endpoints for a specific plan level
level_3_endpoints = EndpointRegistry.get_available_endpoints(3)

# Check if an endpoint requires a specific level
required_level = EndpointRegistry.get_endpoint_requirement("futures.liquidation.get_map")
print(f"Liquidation map requires level {required_level}")

# Get statistics
stats = EndpointRegistry.get_statistics()
print(f"Total endpoints: {stats['total_endpoints']}")
print(f"Free endpoints (Level 1): {stats['free_endpoints']}")
print(f"Premium endpoints (Level 2+): {stats['premium_endpoints']}")
```

## Testing with Plan Levels

The test suite automatically filters endpoints based on your plan level:

```bash
# Set your plan level
export PLAN_LEVEL=3

# Run tests - will only test endpoints available for level 3
python tests/test_all_endpoints.py
```

Output will show:
- ✅ SUCCESS - Endpoint tested successfully
- ⏭️ SKIPPED - Endpoint requires higher plan level
- ❌ FAILED - Endpoint failed (API error)

## Endpoint Requirements by Category

### Always Available (Level 1)
- All basic futures data (prices, open interest, funding rates)
- Spot market data
- Options data (max pain, info)
- ETF data
- Grayscale data
- All index/indicators
- Hyperliquid whale data
- Calendar data

### Startup+ (Level 2)
- `futures.get_whale_index` - Whale activity index
- `futures.liquidation.get_coin_list` - Liquidation by coin

### Standard+ (Level 3)
- `futures.get_coins_markets` - Detailed coin market metrics
- `futures.funding_rate.get_arbitrage` - Funding arbitrage opportunities
- `futures.liquidation.get_order` - Individual liquidation orders
- `futures.orderbook.get_large_limit_order` - Large order tracking
- `futures.rsi.get_list` - RSI indicators
- `spot.get_coins_markets` - Spot market metrics

### Professional+ (Level 4)
- `futures.liquidation.get_map` - Liquidation heatmaps
- `futures.liquidation.get_aggregated_map` - Aggregated liquidation maps
- All liquidation heatmap models (1, 2, 3)

### Enterprise (Level 5)
- Currently no endpoints require Level 5
- Reserved for future premium features

## Migration from String-based Plans

The library maintains backwards compatibility with the old string-based system:

```python
from coinglass.constants import PlanTier  # Deprecated

# Old way (still works but deprecated)
if plan == PlanTier.STANDARD_PLUS:
    # ...

# New way (recommended)
from coinglass.constants import PlanLevel

if plan_level >= PlanLevel.STANDARD:  # Level 3
    # ...
```

## Best Practices

1. **Set PLAN_LEVEL accurately**: Set your plan level to match your CoinGlass subscription to avoid unnecessary API calls to restricted endpoints.

2. **Check access before calling**: Use `check_endpoint_access()` before calling endpoints if you're unsure about access.

3. **Handle access errors gracefully**: Even with plan checking, always handle potential 403 Forbidden errors.

4. **Use endpoint filtering in tests**: When testing, the system will automatically skip endpoints you don't have access to, saving API calls and avoiding errors.

## Example: Building Plan-Aware Applications

```python
from coinglass import CoinGlass
from coinglass.constants import PlanLevel

class TradingBot:
    def __init__(self, api_key: str, plan_level: int):
        self.cg = CoinGlass(api_key=api_key, plan_level=plan_level)
        self.setup_features()
    
    def setup_features(self):
        """Enable features based on plan level."""
        # Basic features for all plans
        self.enable_basic_trading = True
        
        # Advanced features for higher plans
        if self.cg.get_plan_level() >= PlanLevel.STARTUP:
            self.enable_whale_tracking = True
            print("✅ Whale tracking enabled")
        
        if self.cg.get_plan_level() >= PlanLevel.STANDARD:
            self.enable_arbitrage = True
            self.enable_large_orders = True
            print("✅ Arbitrage and large order tracking enabled")
        
        if self.cg.get_plan_level() >= PlanLevel.PROFESSIONAL:
            self.enable_liquidation_maps = True
            print("✅ Liquidation heatmaps enabled")
    
    def get_liquidation_data(self, symbol: str):
        """Get liquidation data based on plan level."""
        # Basic liquidation data (available to all)
        data = {
            'history': self.cg.futures.liquidation.get_history(symbol=symbol)
        }
        
        # Enhanced data for higher plans
        if self.cg.check_endpoint_access("futures.liquidation.get_coin_list"):
            data['by_coin'] = self.cg.futures.liquidation.get_coin_list()
        
        if self.cg.check_endpoint_access("futures.liquidation.get_map"):
            data['heatmap'] = self.cg.futures.liquidation.get_map(symbol=symbol)
        
        return data

# Usage
bot = TradingBot(api_key="your_key", plan_level=3)
```

## Support

For questions about plan levels or to upgrade your plan, visit the [CoinGlass website](https://coinglass.com) or contact their support team.