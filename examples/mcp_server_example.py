#!/usr/bin/env python3
"""
Example MCP (Model Context Protocol) server implementation using CoinGlass API
This demonstrates how to create an MCP server that provides CoinGlass data as tools
"""
import os
import json
import asyncio
from typing import Dict, Any, List, Optional
from datetime import datetime
from coinglass import CoinGlass


class CoinGlassMCPServer:
    """
    MCP Server implementation for CoinGlass API
    
    This example shows how to wrap CoinGlass API endpoints as MCP tools
    that can be used by AI assistants and other MCP clients.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the MCP server with CoinGlass client."""
        self.api_key = api_key or os.getenv('CG_API_KEY')
        if not self.api_key:
            raise ValueError("CoinGlass API key is required")
        
        self.cg = CoinGlass(api_key=self.api_key)
        self.tools = self._register_tools()
    
    def _register_tools(self) -> Dict[str, callable]:
        """Register available tools for the MCP server."""
        return {
            "get_market_overview": self.get_market_overview,
            "get_futures_data": self.get_futures_data,
            "get_liquidations": self.get_liquidations,
            "get_funding_rates": self.get_funding_rates,
            "get_long_short_ratio": self.get_long_short_ratio,
            "get_fear_greed_index": self.get_fear_greed_index,
            "get_bitcoin_indicators": self.get_bitcoin_indicators,
            "get_options_data": self.get_options_data,
            "get_exchange_reserves": self.get_exchange_reserves,
            "get_etf_flows": self.get_etf_flows,
        }
    
    async def get_market_overview(self, symbols: List[str] = None) -> Dict[str, Any]:
        """
        Get market overview for specified symbols or top coins.
        
        Args:
            symbols: List of coin symbols (e.g., ['BTC', 'ETH']). If None, returns top 10.
        
        Returns:
            Market overview data
        """
        try:
            markets = self.cg.futures.get_coins_markets()
            
            if symbols:
                # Filter for requested symbols
                result = [m for m in markets if m['symbol'] in symbols]
            else:
                # Return top 10 by market cap
                result = sorted(markets, key=lambda x: x.get('market_cap_usd', 0), reverse=True)[:10]
            
            return {
                "success": True,
                "data": result,
                "timestamp": datetime.utcnow().isoformat()
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat()
            }
    
    async def get_futures_data(self, symbol: str = "BTC", interval: str = "1h") -> Dict[str, Any]:
        """
        Get comprehensive futures data for a symbol.
        
        Args:
            symbol: Coin symbol (e.g., 'BTC')
            interval: Time interval for historical data
        
        Returns:
            Futures market data including OI, volume, and price
        """
        try:
            result = {}
            
            # Get market data
            markets = self.cg.futures.get_coins_markets()
            coin_data = next((m for m in markets if m['symbol'] == symbol), None)
            if coin_data:
                result['market'] = coin_data
            
            # Get open interest history
            try:
                oi_history = self.cg.futures.open_interest.get_aggregated_history(
                    symbol=symbol,
                    interval=interval
                )
                result['open_interest_history'] = oi_history[:24]  # Last 24 points
            except:
                pass
            
            # Get funding rates
            try:
                funding_rates = self.cg.futures.funding_rate.get_exchange_list(symbol=symbol)
                result['funding_rates'] = funding_rates
            except:
                pass
            
            return {
                "success": True,
                "data": result,
                "timestamp": datetime.utcnow().isoformat()
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat()
            }
    
    async def get_liquidations(self, symbol: str = "BTC", interval: str = "1h") -> Dict[str, Any]:
        """
        Get liquidation data for a symbol.
        
        Args:
            symbol: Coin symbol
            interval: Time interval
        
        Returns:
            Liquidation data
        """
        try:
            # Get 24h liquidation summary from market data
            markets = self.cg.futures.get_coins_markets()
            coin_data = next((m for m in markets if m['symbol'] == symbol), None)
            
            result = {}
            if coin_data:
                result['24h_summary'] = {
                    'total': coin_data.get('liquidation_usd_24h', 0),
                    'long': coin_data.get('long_liquidation_usd_24h', 0),
                    'short': coin_data.get('short_liquidation_usd_24h', 0)
                }
            
            # Try to get historical data
            try:
                history = self.cg.futures.liquidation.get_aggregated_history(
                    symbol=symbol,
                    interval=interval
                )
                result['history'] = history[:24]  # Last 24 points
            except:
                pass
            
            return {
                "success": True,
                "data": result,
                "timestamp": datetime.utcnow().isoformat()
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat()
            }
    
    async def get_funding_rates(self, symbol: str = "BTC") -> Dict[str, Any]:
        """Get current funding rates across exchanges."""
        try:
            funding_rates = self.cg.futures.funding_rate.get_exchange_list(symbol=symbol)
            
            # Calculate statistics
            if funding_rates:
                rates = [fr.get('funding_rate', 0) for fr in funding_rates]
                avg_rate = sum(rates) / len(rates)
                max_rate = max(rates)
                min_rate = min(rates)
                
                result = {
                    'average': avg_rate,
                    'max': max_rate,
                    'min': min_rate,
                    'spread': max_rate - min_rate,
                    'exchanges': funding_rates
                }
            else:
                result = {'error': 'No funding rate data available'}
            
            return {
                "success": True,
                "data": result,
                "timestamp": datetime.utcnow().isoformat()
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat()
            }
    
    async def get_long_short_ratio(self, symbol: str = "BTC") -> Dict[str, Any]:
        """Get long/short ratio data."""
        try:
            markets = self.cg.futures.get_coins_markets()
            coin_data = next((m for m in markets if m['symbol'] == symbol), None)
            
            if coin_data:
                ls_ratio = coin_data.get('long_short_ratio_24h', 1.0)
                result = {
                    'ratio': ls_ratio,
                    'sentiment': 'BULLISH' if ls_ratio > 1 else 'BEARISH',
                    'strength': abs(ls_ratio - 1) * 100  # Percentage deviation from neutral
                }
            else:
                result = {'error': 'No data available for symbol'}
            
            return {
                "success": True,
                "data": result,
                "timestamp": datetime.utcnow().isoformat()
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat()
            }
    
    async def get_fear_greed_index(self) -> Dict[str, Any]:
        """Get Fear and Greed Index."""
        try:
            fear_greed = self.cg.index.get_fear_greed_history()
            
            if fear_greed and isinstance(fear_greed, list):
                latest = fear_greed[-1]
                # Get last 7 days for trend
                week_data = fear_greed[-7:] if len(fear_greed) >= 7 else fear_greed
                
                result = {
                    'current': latest,
                    'week_average': sum(d.get('value', 0) for d in week_data) / len(week_data),
                    'week_data': week_data
                }
            else:
                result = {'error': 'No Fear & Greed data available'}
            
            return {
                "success": True,
                "data": result,
                "timestamp": datetime.utcnow().isoformat()
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat()
            }
    
    async def get_bitcoin_indicators(self) -> Dict[str, Any]:
        """Get various Bitcoin indicators."""
        indicators = {}
        
        # Try to get each indicator
        try:
            indicators['ahr999'] = self.cg.get_ahr999()
        except:
            pass
        
        try:
            indicators['pi_cycle'] = self.cg.get_pi_cycle_top_indicator()
        except:
            pass
        
        try:
            indicators['puell_multiple'] = self.cg.get_puell_multiple()
        except:
            pass
        
        try:
            indicators['stock_to_flow'] = self.cg.get_stock_to_flow()
        except:
            pass
        
        return {
            "success": True,
            "data": indicators,
            "timestamp": datetime.utcnow().isoformat()
        }
    
    async def get_options_data(self, symbol: str = "BTC") -> Dict[str, Any]:
        """Get options market data."""
        try:
            result = {}
            
            # Get max pain
            try:
                max_pain = self.cg.option.get_max_pain(symbol=symbol)
                result['max_pain'] = max_pain
            except:
                pass
            
            # Get options info
            try:
                info = self.cg.option.get_info(symbol=symbol)
                result['info'] = info
            except:
                pass
            
            return {
                "success": True,
                "data": result,
                "timestamp": datetime.utcnow().isoformat()
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat()
            }
    
    async def get_exchange_reserves(self, exchange: str = "Binance") -> Dict[str, Any]:
        """Get exchange on-chain reserves."""
        try:
            assets = self.cg.exchange.get_assets(exchange=exchange)
            
            # Calculate total value
            total_usd = sum(a.get('reserve_usd', 0) for a in assets)
            
            # Get top assets
            top_assets = sorted(assets, key=lambda x: x.get('reserve_usd', 0), reverse=True)[:10]
            
            result = {
                'exchange': exchange,
                'total_reserves_usd': total_usd,
                'top_assets': top_assets,
                'total_assets': len(assets)
            }
            
            return {
                "success": True,
                "data": result,
                "timestamp": datetime.utcnow().isoformat()
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat()
            }
    
    async def get_etf_flows(self) -> Dict[str, Any]:
        """Get ETF flow data."""
        try:
            result = {}
            
            # Get Bitcoin ETF data
            try:
                btc_etfs = self.cg.etf.bitcoin.get_list()
                btc_flows = self.cg.etf.bitcoin.get_flow_history()
                result['bitcoin'] = {
                    'etf_count': len(btc_etfs),
                    'etfs': btc_etfs,
                    'recent_flows': btc_flows[:7] if btc_flows else []
                }
            except:
                pass
            
            # Get Ethereum ETF data
            try:
                eth_etfs = self.cg.etf.ethereum.get_list()
                eth_flows = self.cg.etf.ethereum.get_flow_history()
                result['ethereum'] = {
                    'etf_count': len(eth_etfs),
                    'etfs': eth_etfs,
                    'recent_flows': eth_flows[:7] if eth_flows else []
                }
            except:
                pass
            
            return {
                "success": True,
                "data": result,
                "timestamp": datetime.utcnow().isoformat()
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat()
            }
    
    async def handle_tool_call(self, tool_name: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Handle a tool call from an MCP client.
        
        Args:
            tool_name: Name of the tool to execute
            params: Parameters for the tool
        
        Returns:
            Tool execution result
        """
        if tool_name not in self.tools:
            return {
                "success": False,
                "error": f"Unknown tool: {tool_name}",
                "available_tools": list(self.tools.keys())
            }
        
        tool = self.tools[tool_name]
        params = params or {}
        
        try:
            # Execute the tool
            result = await tool(**params)
            return result
        except Exception as e:
            return {
                "success": False,
                "error": f"Tool execution failed: {str(e)}",
                "tool": tool_name,
                "params": params
            }
    
    def get_tool_descriptions(self) -> List[Dict[str, Any]]:
        """Get descriptions of all available tools."""
        return [
            {
                "name": "get_market_overview",
                "description": "Get market overview for cryptocurrencies",
                "parameters": {
                    "symbols": {"type": "array", "description": "List of coin symbols", "required": False}
                }
            },
            {
                "name": "get_futures_data",
                "description": "Get comprehensive futures market data",
                "parameters": {
                    "symbol": {"type": "string", "description": "Coin symbol", "default": "BTC"},
                    "interval": {"type": "string", "description": "Time interval", "default": "1h"}
                }
            },
            {
                "name": "get_liquidations",
                "description": "Get liquidation data",
                "parameters": {
                    "symbol": {"type": "string", "description": "Coin symbol", "default": "BTC"},
                    "interval": {"type": "string", "description": "Time interval", "default": "1h"}
                }
            },
            {
                "name": "get_funding_rates",
                "description": "Get funding rates across exchanges",
                "parameters": {
                    "symbol": {"type": "string", "description": "Coin symbol", "default": "BTC"}
                }
            },
            {
                "name": "get_long_short_ratio",
                "description": "Get long/short ratio and market sentiment",
                "parameters": {
                    "symbol": {"type": "string", "description": "Coin symbol", "default": "BTC"}
                }
            },
            {
                "name": "get_fear_greed_index",
                "description": "Get Fear and Greed Index",
                "parameters": {}
            },
            {
                "name": "get_bitcoin_indicators",
                "description": "Get various Bitcoin indicators",
                "parameters": {}
            },
            {
                "name": "get_options_data",
                "description": "Get options market data",
                "parameters": {
                    "symbol": {"type": "string", "description": "Coin symbol", "default": "BTC"}
                }
            },
            {
                "name": "get_exchange_reserves",
                "description": "Get exchange on-chain reserves",
                "parameters": {
                    "exchange": {"type": "string", "description": "Exchange name", "default": "Binance"}
                }
            },
            {
                "name": "get_etf_flows",
                "description": "Get ETF flow data",
                "parameters": {}
            }
        ]
    
    def close(self):
        """Clean up resources."""
        self.cg.close()


async def main():
    """Example usage of the MCP server."""
    print("CoinGlass MCP Server Example")
    print("=" * 50)
    
    # Initialize the server
    server = CoinGlassMCPServer()
    
    try:
        # Example tool calls
        print("\n1. Getting market overview...")
        result = await server.handle_tool_call("get_market_overview", {"symbols": ["BTC", "ETH"]})
        if result['success']:
            print(f"   Found {len(result['data'])} markets")
        
        print("\n2. Getting Bitcoin futures data...")
        result = await server.handle_tool_call("get_futures_data", {"symbol": "BTC"})
        if result['success'] and 'market' in result['data']:
            market = result['data']['market']
            print(f"   BTC Price: ${market['current_price']:,.2f}")
            print(f"   Open Interest: ${market.get('open_interest_usd', 0):,.0f}")
        
        print("\n3. Getting Fear & Greed Index...")
        result = await server.handle_tool_call("get_fear_greed_index")
        if result['success'] and 'current' in result['data']:
            current = result['data']['current']
            print(f"   Current Value: {current.get('value', 'N/A')}")
            print(f"   Classification: {current.get('classification', 'N/A')}")
        
        print("\n4. Getting funding rates...")
        result = await server.handle_tool_call("get_funding_rates", {"symbol": "BTC"})
        if result['success']:
            data = result['data']
            print(f"   Average Rate: {data.get('average', 0):.6f}")
            print(f"   Spread: {data.get('spread', 0):.6f}")
        
        print("\n5. Available tools:")
        for tool in server.get_tool_descriptions():
            print(f"   - {tool['name']}: {tool['description']}")
        
        print("\n" + "=" * 50)
        print("MCP Server example complete!")
        
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        server.close()


if __name__ == "__main__":
    asyncio.run(main())