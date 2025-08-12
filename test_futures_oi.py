#!/usr/bin/env python3
"""Test futures open interest endpoints specifically"""

from coinglass import CoinGlass
import os
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize client
api_key = os.getenv('CG_API_KEY')
cg = CoinGlass(api_key)

print("Testing futures.open_interest.get_history...")
try:
    result = cg.futures.open_interest.get_history(exchange="Binance", symbol="BTCUSDT", interval="4h")
    print(f"✅ Success - got {len(result) if isinstance(result, list) else 'data'}")
except Exception as e:
    print(f"❌ Error: {e}")
time.sleep(0.25)

print("\nTesting futures.open_interest.get_aggregated_history...")
try:
    result = cg.futures.open_interest.get_aggregated_history(symbol="BTC", interval="1d")
    print(f"✅ Success - got {len(result) if isinstance(result, list) else 'data'}")
except Exception as e:
    print(f"❌ Error: {e}")
time.sleep(0.25)

print("\nTesting futures.open_interest.get_aggregated_stablecoin_margin_history...")
try:
    result = cg.futures.open_interest.get_aggregated_stablecoin_margin_history(symbol="BTC", interval="4h")
    print(f"✅ Success - got {len(result) if isinstance(result, list) else 'data'}")
except Exception as e:
    print(f"❌ Error: {e}")
time.sleep(0.25)

print("\nTesting futures.open_interest.get_aggregated_coin_margin_history...")
try:
    result = cg.futures.open_interest.get_aggregated_coin_margin_history(symbol="BTC", interval="4h")
    print(f"✅ Success - got {len(result) if isinstance(result, list) else 'data'}")
except Exception as e:
    print(f"❌ Error: {e}")
time.sleep(0.25)

print("\nTesting futures.open_interest.get_exchange_list...")
try:
    result = cg.futures.open_interest.get_exchange_list(symbol="BTC")
    print(f"✅ Success - got data")
except Exception as e:
    print(f"❌ Error: {e}")