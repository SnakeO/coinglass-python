#!/usr/bin/env python3
"""
Futures trading analysis examples using CoinGlass API
"""
import os
from datetime import datetime, timedelta
from coinglass import CoinGlass


def analyze_futures_market(cg: CoinGlass, symbol: str = "BTC"):
    """Comprehensive futures market analysis for a given symbol."""
    
    print(f"\n{'='*60}")
    print(f"FUTURES MARKET ANALYSIS: {symbol}")
    print(f"{'='*60}")
    
    # 1. Market Overview
    print(f"\n1. MARKET OVERVIEW")
    print("-" * 40)
    markets = cg.futures.get_coins_markets()
    coin_data = next((m for m in markets if m['symbol'] == symbol), None)
    
    if coin_data:
        print(f"Current Price: ${coin_data['current_price']:,.2f}")
        print(f"24h Change: {coin_data.get('price_change_percent_24h', 0):.2f}%")
        print(f"Market Cap: ${coin_data.get('market_cap_usd', 0):,.0f}")
        print(f"Open Interest: ${coin_data.get('open_interest_usd', 0):,.0f}")
        print(f"OI/MCap Ratio: {coin_data.get('open_interest_market_cap_ratio', 0):.4f}")
        print(f"24h Volume: ${coin_data.get('volume_usd', 0):,.0f}")
        print(f"OI/Volume Ratio: {coin_data.get('open_interest_volume_ratio', 0):.4f}")
    
    # 2. Funding Rates
    print(f"\n2. FUNDING RATES")
    print("-" * 40)
    try:
        funding_rates = cg.futures.funding_rate.get_exchange_list(symbol=symbol)
        if funding_rates:
            avg_rate = sum(fr.get('funding_rate', 0) for fr in funding_rates) / len(funding_rates)
            print(f"Average Funding Rate: {avg_rate:.6f}")
            print(f"Top 3 Exchanges:")
            for fr in sorted(funding_rates, key=lambda x: x.get('funding_rate', 0), reverse=True)[:3]:
                print(f"  {fr.get('exchange', 'Unknown')}: {fr.get('funding_rate', 0):.6f}")
    except Exception as e:
        print(f"Error fetching funding rates: {e}")
    
    # 3. Long/Short Ratios
    print(f"\n3. LONG/SHORT RATIOS")
    print("-" * 40)
    if coin_data:
        ls_ratio = coin_data.get('long_short_ratio_24h', 1.0)
        print(f"24h Long/Short Ratio: {ls_ratio:.4f}")
        if ls_ratio > 1:
            print(f"Market Sentiment: BULLISH ({(ls_ratio-1)*100:.2f}% more longs)")
        else:
            print(f"Market Sentiment: BEARISH ({(1-ls_ratio)*100:.2f}% more shorts)")
    
    # 4. Liquidations
    print(f"\n4. LIQUIDATIONS (24h)")
    print("-" * 40)
    if coin_data:
        total_liq = coin_data.get('liquidation_usd_24h', 0)
        long_liq = coin_data.get('long_liquidation_usd_24h', 0)
        short_liq = coin_data.get('short_liquidation_usd_24h', 0)
        
        print(f"Total Liquidations: ${total_liq:,.0f}")
        print(f"Long Liquidations: ${long_liq:,.0f} ({long_liq/total_liq*100:.1f}%)" if total_liq > 0 else "Long Liquidations: $0")
        print(f"Short Liquidations: ${short_liq:,.0f} ({short_liq/total_liq*100:.1f}%)" if total_liq > 0 else "Short Liquidations: $0")
    
    # 5. Open Interest by Exchange
    print(f"\n5. OPEN INTEREST BY EXCHANGE")
    print("-" * 40)
    try:
        oi_exchange = cg.futures.open_interest.get_exchange_list(symbol=symbol)
        if oi_exchange and 'stablecoin_margin_list' in oi_exchange:
            stablecoin_oi = oi_exchange['stablecoin_margin_list']
            print("Top 5 Exchanges (Stablecoin-margined):")
            for ex in sorted(stablecoin_oi, key=lambda x: x.get('open_interest', 0), reverse=True)[:5]:
                print(f"  {ex.get('exchange', 'Unknown')}: ${ex.get('open_interest', 0):,.0f}")
    except Exception as e:
        print(f"Error fetching OI by exchange: {e}")


def analyze_trading_pairs(cg: CoinGlass):
    """Analyze top trading pairs across exchanges."""
    
    print(f"\n{'='*60}")
    print(f"TOP FUTURES TRADING PAIRS ANALYSIS")
    print(f"{'='*60}")
    
    pairs = cg.futures.get_pairs_markets()
    
    # Sort by volume
    top_pairs = sorted(pairs, key=lambda x: x.get('volume_usd', 0), reverse=True)[:10]
    
    print(f"\nTOP 10 PAIRS BY VOLUME:")
    print("-" * 40)
    for i, pair in enumerate(top_pairs, 1):
        print(f"{i:2}. {pair.get('symbol', 'Unknown'):15} "
              f"@ {pair.get('exchange_name', 'Unknown'):10} "
              f"Vol: ${pair.get('volume_usd', 0):,.0f}")
    
    # Find pairs with highest funding rates
    print(f"\nHIGHEST FUNDING RATES:")
    print("-" * 40)
    funded_pairs = [p for p in pairs if p.get('funding_rate')]
    top_funded = sorted(funded_pairs, key=lambda x: abs(x.get('funding_rate', 0)), reverse=True)[:5]
    for pair in top_funded:
        print(f"{pair.get('symbol', 'Unknown'):15} "
              f"@ {pair.get('exchange_name', 'Unknown'):10} "
              f"Rate: {pair.get('funding_rate', 0):.6f}")
    
    # Find pairs with highest OI/Volume ratio
    print(f"\nHIGHEST OI/VOLUME RATIO (Potential Squeeze):")
    print("-" * 40)
    oi_vol_pairs = [p for p in pairs if p.get('open_interest_volume_ratio')]
    top_oi_vol = sorted(oi_vol_pairs, key=lambda x: x.get('open_interest_volume_ratio', 0), reverse=True)[:5]
    for pair in top_oi_vol:
        print(f"{pair.get('symbol', 'Unknown'):15} "
              f"@ {pair.get('exchange_name', 'Unknown'):10} "
              f"Ratio: {pair.get('open_interest_volume_ratio', 0):.4f}")


def main():
    # Initialize the client
    api_key = os.getenv('CG_API_KEY', 'your_api_key_here')
    
    with CoinGlass(api_key=api_key) as cg:
        try:
            # Analyze BTC futures
            analyze_futures_market(cg, "BTC")
            
            # Analyze ETH futures
            analyze_futures_market(cg, "ETH")
            
            # Analyze top trading pairs
            analyze_trading_pairs(cg)
            
            print(f"\n{'='*60}")
            print("Analysis complete!")
            print(f"{'='*60}")
            
        except Exception as e:
            print(f"\nError during analysis: {e}")
            print("Please check your API key and connection.")


if __name__ == "__main__":
    main()