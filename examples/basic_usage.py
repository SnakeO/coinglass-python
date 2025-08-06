#!/usr/bin/env python3
"""
Basic usage examples for the CoinGlass Python library
"""
import os
import json
from datetime import datetime
from coinglass import CoinGlass


def main():
    # Initialize the client
    # You can set your API key as an environment variable: CG_API_KEY
    # Or pass it directly
    api_key = os.getenv('CG_API_KEY', 'your_api_key_here')
    
    # Create CoinGlass client
    cg = CoinGlass(api_key=api_key)
    
    print("=" * 50)
    print("CoinGlass API - Basic Usage Examples")
    print("=" * 50)
    
    try:
        # 1. Get supported futures coins
        print("\n1. Supported Futures Coins:")
        print("-" * 30)
        coins = cg.futures.get_supported_coins()
        print(f"Total supported coins: {len(coins)}")
        print(f"Top 10 coins: {coins[:10]}")
        
        # 2. Get futures market data
        print("\n2. Futures Market Overview:")
        print("-" * 30)
        markets = cg.futures.get_coins_markets()
        
        # Find BTC and ETH data
        btc_data = next((m for m in markets if m['symbol'] == 'BTC'), None)
        eth_data = next((m for m in markets if m['symbol'] == 'ETH'), None)
        
        if btc_data:
            print(f"BTC:")
            print(f"  Price: ${btc_data['current_price']:,.2f}")
            print(f"  24h Change: {btc_data.get('price_change_percent_24h', 0):.2f}%")
            print(f"  Open Interest: ${btc_data.get('open_interest_usd', 0):,.0f}")
            print(f"  24h Volume: ${btc_data.get('volume_usd', 0):,.0f}")
        
        if eth_data:
            print(f"\nETH:")
            print(f"  Price: ${eth_data['current_price']:,.2f}")
            print(f"  24h Change: {eth_data.get('price_change_percent_24h', 0):.2f}%")
            print(f"  Open Interest: ${eth_data.get('open_interest_usd', 0):,.0f}")
            print(f"  24h Volume: ${eth_data.get('volume_usd', 0):,.0f}")
        
        # 3. Get Fear and Greed Index
        print("\n3. Fear and Greed Index:")
        print("-" * 30)
        fear_greed = cg.index.get_fear_greed_history()
        if fear_greed:
            latest = fear_greed[-1] if isinstance(fear_greed, list) else fear_greed
            if isinstance(latest, dict):
                print(f"Current Value: {latest.get('value', 'N/A')}")
                print(f"Classification: {latest.get('classification', 'N/A')}")
        
        # 4. Get exchange ranking
        print("\n4. Exchange Ranking by Open Interest:")
        print("-" * 30)
        exchange_rank = cg.futures.get_exchange_rank()
        if exchange_rank:
            for i, exchange in enumerate(exchange_rank[:5], 1):
                print(f"{i}. {exchange.get('exchange', 'Unknown')}: "
                      f"${exchange.get('open_interest_usd', 0):,.0f}")
        
        # 5. Get Bitcoin indicators
        print("\n5. Bitcoin Indicators:")
        print("-" * 30)
        
        # AHR999
        try:
            ahr999 = cg.get_ahr999()
            if isinstance(ahr999, dict):
                print(f"AHR999 Index: {ahr999.get('value', 'N/A')}")
        except Exception as e:
            print(f"AHR999: Error - {e}")
        
        # Get spot markets
        print("\n6. Spot Markets:")
        print("-" * 30)
        spot_markets = cg.spot.get_pairs_markets()
        if spot_markets:
            # Get top 3 by volume
            sorted_markets = sorted(
                spot_markets, 
                key=lambda x: x.get('volume_usd', 0), 
                reverse=True
            )[:3]
            for market in sorted_markets:
                print(f"{market.get('symbol', 'Unknown')}: "
                      f"${market.get('current_price', 0):,.2f} "
                      f"(Vol: ${market.get('volume_usd', 0):,.0f})")
        
        # 7. Get ETF data
        print("\n7. Bitcoin ETF Data:")
        print("-" * 30)
        try:
            btc_etfs = cg.etf.bitcoin.get_list()
            if btc_etfs:
                print(f"Total Bitcoin ETFs: {len(btc_etfs)}")
                for etf in btc_etfs[:3]:
                    print(f"  - {etf.get('ticker', 'Unknown')}: "
                          f"{etf.get('name', 'Unknown')}")
        except Exception as e:
            print(f"ETF Data: Error - {e}")
        
        print("\n" + "=" * 50)
        print("Examples completed successfully!")
        print("=" * 50)
        
    except Exception as e:
        print(f"\nError: {e}")
        print("\nMake sure you have set a valid API key.")
    
    finally:
        # Clean up
        cg.close()


if __name__ == "__main__":
    main()