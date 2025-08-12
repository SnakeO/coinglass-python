#!/usr/bin/env python3
"""Test sample of fixed endpoints"""

from coinglass import CoinGlass
import os
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize client
api_key = os.getenv('CG_API_KEY')
cg = CoinGlass(api_key)

tests = [
    ("futures.get_basis", lambda: cg.futures.get_basis(exchange="Binance", symbol="BTCUSDT", interval="1h")),
    ("futures.get_whale_index", lambda: cg.futures.get_whale_index(exchange="Binance", symbol="BTCUSDT", interval="1h")),
    ("futures.price.get_history", lambda: cg.futures.price.get_history(symbol="BTCUSDT", interval="1h", exchange="Binance")),
    ("futures.open_interest.get_history", lambda: cg.futures.open_interest.get_history(exchange="Binance", symbol="BTCUSDT", interval="4h")),
    ("futures.funding_rate.get_history", lambda: cg.futures.funding_rate.get_history(exchange="Binance", symbol="BTCUSDT", interval="8h")),
    ("futures.liquidation.get_history", lambda: cg.futures.liquidation.get_history(exchange="Binance", symbol="BTCUSDT", interval="1h")),
    ("futures.taker_buy_sell_volume.get_history", lambda: cg.futures.taker_buy_sell_volume.get_history(exchange="Binance", symbol="BTCUSDT", interval="1h")),
    ("futures.taker_buy_sell_volume.get_exchange_list", lambda: cg.futures.taker_buy_sell_volume.get_exchange_list(symbol="BTCUSDT", range="4h")),
]

print("Testing fixed endpoints...")
print("=" * 60)

success_count = 0
for name, test_func in tests:
    print(f"Testing {name}...", end=" ")
    try:
        result = test_func()
        if result is not None:
            print("✅ SUCCESS")
            success_count += 1
        else:
            print("❌ FAILED - No data returned")
    except Exception as e:
        print(f"❌ FAILED - {str(e)[:50]}")
    
    # Add delay between API calls to avoid rate limiting
    time.sleep(0.25)

print("=" * 60)
print(f"Results: {success_count}/{len(tests)} tests passed ({success_count*100//len(tests)}%)")