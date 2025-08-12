#!/usr/bin/env python3
"""Quick test for two specific endpoints"""

from coinglass import CoinGlass
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize client
api_key = os.getenv('CG_API_KEY')
cg = CoinGlass(api_key)

print("Testing futures.get_basis with {'symbol': 'BTC'}...")
try:
    result = cg.futures.get_basis(symbol="BTC")
    print(f"✅ Success: {result}")
except Exception as e:
    print(f"❌ Error: {e}")

print("\nTesting futures.get_whale_index with no params...")
try:
    result = cg.futures.get_whale_index()
    print(f"✅ Success: {result}")
except Exception as e:
    print(f"❌ Error: {e}")

print("\nTesting futures.get_basis with all params...")
try:
    result = cg.futures.get_basis(exchange="Binance", symbol="BTC", interval="1h")
    print(f"✅ Success: {result}")
except Exception as e:
    print(f"❌ Error: {e}")

print("\nTesting futures.get_whale_index with all params...")
try:
    result = cg.futures.get_whale_index(exchange="Binance", symbol="BTC", interval="1h")
    print(f"✅ Success: {result}")
except Exception as e:
    print(f"❌ Error: {e}")