#!/usr/bin/env python3
"""
Quick test to verify plan level filtering is working correctly.
"""
import os
from dotenv import load_dotenv
from coinglass import CoinGlass
from coinglass.constants import PlanLevel
from coinglass.endpoints import EndpointRegistry

# Load environment variables
load_dotenv()

def test_plan_filtering():
    """Test that plan level filtering works correctly."""
    
    # Get plan level from environment
    plan_level = int(os.getenv('PLAN_LEVEL', '1'))
    print(f"\n🔍 Testing with PLAN_LEVEL={plan_level} ({PlanLevel.get_name(plan_level)})")
    print("=" * 60)
    
    # Initialize CoinGlass (will use PLAN_LEVEL from env)
    cg = CoinGlass(api_key=os.getenv('CG_API_KEY'))
    
    # Verify plan level was loaded correctly
    assert cg.get_plan_level() == plan_level, f"Expected plan level {plan_level}, got {cg.get_plan_level()}"
    print(f"✅ CoinGlass initialized with Level {cg.get_plan_level()}")
    
    # Get available endpoints
    available = cg.get_available_endpoints()
    print(f"✅ Available endpoints: {len(available)}")
    
    # Test some specific endpoints based on plan level
    test_cases = [
        ("futures.get_supported_coins", 1, "Basic endpoint"),
        ("futures.get_whale_index", 2, "Startup+ endpoint"),
        ("futures.get_coins_markets", 3, "Standard+ endpoint"),
        ("futures.liquidation.get_map", 4, "Professional+ endpoint"),
    ]
    
    print(f"\n📊 Testing endpoint access for Level {plan_level}:")
    print("-" * 60)
    
    for endpoint, required_level, description in test_cases:
        has_access = cg.check_endpoint_access(endpoint)
        expected_access = plan_level >= required_level
        
        if has_access == expected_access:
            status = "✅"
        else:
            status = "❌"
        
        access_str = "YES" if has_access else "NO"
        print(f"{status} {endpoint:<40} Access: {access_str:<3} ({description})")
    
    # Show statistics
    stats = cg.get_endpoint_statistics()
    print(f"\n📈 Statistics for {stats['current_plan_name']} (Level {stats['current_plan_level']}):")
    print("-" * 60)
    print(f"Available endpoints: {stats['available_endpoints_count']} / {stats['total_endpoints']}")
    print(f"Coverage: {stats['available_endpoints_count']/stats['total_endpoints']*100:.1f}%")
    
    # Show breakdown by plan
    print(f"\n📊 Endpoint distribution by plan level:")
    for level_name, count in stats['by_plan_level'].items():
        print(f"  {level_name:<15} {count:>3} endpoints")
    
    # Test actual API call with an endpoint we should have access to
    print(f"\n🔄 Testing actual API call...")
    try:
        # This should work for Level 2
        result = cg.futures.get_supported_coins()
        if result:
            print(f"✅ Successfully called futures.get_supported_coins()")
            print(f"   Retrieved {len(result)} coins")
    except Exception as e:
        print(f"❌ Failed to call endpoint: {e}")
    
    # Test an endpoint we shouldn't have access to (if plan < 3)
    if plan_level < 3:
        print(f"\n🔄 Testing restricted endpoint (should fail gracefully)...")
        try:
            # This requires Level 3
            result = cg.futures.get_coins_markets()
            print(f"⚠️  Unexpected success calling futures.get_coins_markets()")
        except Exception as e:
            if "403" in str(e) or "forbidden" in str(e).lower():
                print(f"✅ Correctly blocked: {str(e)[:100]}")
            else:
                print(f"❓ Got error: {str(e)[:100]}")
    
    print("\n" + "=" * 60)
    print("✅ Plan level filtering test complete!")

if __name__ == "__main__":
    test_plan_filtering()