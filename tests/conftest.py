"""
Pytest configuration and fixtures for CoinGlass tests
"""
import os
import pytest
from unittest.mock import Mock, MagicMock
from coinglass import CoinGlass, CoinGlassClient


@pytest.fixture
def api_key():
    """Provide test API key."""
    return os.getenv('CG_API_KEY', 'test_api_key')


@pytest.fixture
def mock_client():
    """Create a mock CoinGlassClient."""
    client = Mock(spec=CoinGlassClient)
    client.get = MagicMock(return_value={'code': '0', 'msg': 'success', 'data': []})
    client.post = MagicMock(return_value={'code': '0', 'msg': 'success', 'data': {}})
    return client


@pytest.fixture
def coinglass_client(api_key):
    """Create a CoinGlassClient instance."""
    return CoinGlassClient(api_key=api_key)


@pytest.fixture
def coinglass(api_key):
    """Create a CoinGlass instance."""
    return CoinGlass(api_key=api_key)


@pytest.fixture
def sample_market_data():
    """Sample market data response."""
    return {
        'code': '0',
        'msg': 'success',
        'data': [
            {
                'symbol': 'BTC',
                'current_price': 85000.0,
                'price_change_percent_24h': 2.5,
                'market_cap_usd': 1650000000000,
                'open_interest_usd': 55000000000,
                'volume_usd': 70000000000
            },
            {
                'symbol': 'ETH',
                'current_price': 1600.0,
                'price_change_percent_24h': 3.2,
                'market_cap_usd': 190000000000,
                'open_interest_usd': 15000000000,
                'volume_usd': 25000000000
            }
        ]
    }


@pytest.fixture
def sample_funding_rate_data():
    """Sample funding rate data."""
    return {
        'code': '0',
        'msg': 'success',
        'data': [
            {'exchange': 'Binance', 'funding_rate': 0.0010},
            {'exchange': 'OKX', 'funding_rate': 0.0012},
            {'exchange': 'Bybit', 'funding_rate': 0.0008}
        ]
    }


@pytest.fixture
def sample_ohlc_data():
    """Sample OHLC data."""
    return {
        'code': '0',
        'msg': 'success',
        'data': [
            {
                'time': 1700000000000,
                'open': '84000',
                'high': '85500',
                'low': '83500',
                'close': '85000',
                'volume_usd': '1000000000'
            },
            {
                'time': 1700003600000,
                'open': '85000',
                'high': '86000',
                'low': '84500',
                'close': '85500',
                'volume_usd': '1100000000'
            }
        ]
    }