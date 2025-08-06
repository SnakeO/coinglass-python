"""
Tests for the Futures API module
"""
import pytest
from unittest.mock import Mock, patch
from coinglass.futures import FuturesAPI


class TestFuturesAPI:
    """Test FuturesAPI class."""
    
    def test_futures_api_initialization(self, mock_client):
        """Test FuturesAPI initialization."""
        futures = FuturesAPI(mock_client)
        assert futures.client == mock_client
        assert hasattr(futures, 'price')
        assert hasattr(futures, 'open_interest')
        assert hasattr(futures, 'funding_rate')
        assert hasattr(futures, 'liquidation')
    
    def test_get_supported_coins(self, mock_client):
        """Test get_supported_coins method."""
        mock_client.get.return_value = {
            'code': '0',
            'msg': 'success',
            'data': ['BTC', 'ETH', 'SOL']
        }
        
        futures = FuturesAPI(mock_client)
        coins = futures.get_supported_coins()
        
        assert coins == ['BTC', 'ETH', 'SOL']
        mock_client.get.assert_called_once_with('/futures/supported-coins')
    
    def test_get_coins_markets(self, mock_client, sample_market_data):
        """Test get_coins_markets method."""
        mock_client.get.return_value = sample_market_data
        
        futures = FuturesAPI(mock_client)
        markets = futures.get_coins_markets()
        
        assert len(markets) == 2
        assert markets[0]['symbol'] == 'BTC'
        assert markets[0]['current_price'] == 85000.0
        mock_client.get.assert_called_once_with('/futures/coins-markets')
    
    def test_get_pairs_markets(self, mock_client):
        """Test get_pairs_markets method."""
        mock_data = {
            'code': '0',
            'msg': 'success',
            'data': [
                {
                    'instrument_id': 'BTCUSDT',
                    'exchange_name': 'Binance',
                    'current_price': 85000.0
                }
            ]
        }
        mock_client.get.return_value = mock_data
        
        futures = FuturesAPI(mock_client)
        pairs = futures.get_pairs_markets()
        
        assert len(pairs) == 1
        assert pairs[0]['instrument_id'] == 'BTCUSDT'
        mock_client.get.assert_called_once_with('/futures/pairs-markets')
    
    def test_get_exchange_rank(self, mock_client):
        """Test get_exchange_rank method."""
        mock_data = {
            'code': '0',
            'msg': 'success',
            'data': [
                {'exchange': 'Binance', 'open_interest_usd': 60000000000},
                {'exchange': 'OKX', 'open_interest_usd': 25000000000}
            ]
        }
        mock_client.get.return_value = mock_data
        
        futures = FuturesAPI(mock_client)
        rank = futures.get_exchange_rank()
        
        assert len(rank) == 2
        assert rank[0]['exchange'] == 'Binance'
        mock_client.get.assert_called_once_with('/futures/exchange-rank')
    
    def test_get_basis(self, mock_client):
        """Test get_basis method."""
        mock_data = {
            'code': '0',
            'msg': 'success',
            'data': {'basis': 0.05}
        }
        mock_client.get.return_value = mock_data
        
        futures = FuturesAPI(mock_client)
        
        # Test without symbol
        basis = futures.get_basis()
        assert basis == {'basis': 0.05}
        mock_client.get.assert_called_with('/futures/basis', params={})
        
        # Test with symbol
        mock_client.reset_mock()
        basis = futures.get_basis(symbol='BTC')
        mock_client.get.assert_called_with('/futures/basis', params={'symbol': 'BTC'})
    
    def test_price_history(self, mock_client, sample_ohlc_data):
        """Test price history endpoint."""
        mock_client.get.return_value = sample_ohlc_data
        
        futures = FuturesAPI(mock_client)
        history = futures.price.get_history(symbol='BTC', interval='1h')
        
        assert len(history) == 2
        assert history[0]['time'] == 1700000000000
        mock_client.get.assert_called_once_with(
            '/futures/price/history',
            params={'symbol': 'BTC', 'interval': '1h'}
        )
    
    def test_open_interest_history(self, mock_client):
        """Test open interest history endpoint."""
        mock_data = {
            'code': '0',
            'msg': 'success',
            'data': [
                {'time': 1700000000000, 'open': '50000000000', 'close': '51000000000'}
            ]
        }
        mock_client.get.return_value = mock_data
        
        futures = FuturesAPI(mock_client)
        oi_history = futures.open_interest.get_history(
            symbol='BTCUSDT_PERP',
            interval='4h'
        )
        
        assert len(oi_history) == 1
        mock_client.get.assert_called_once_with(
            '/futures/open-interest/history',
            params={'symbol': 'BTCUSDT_PERP', 'interval': '4h'}
        )
    
    def test_funding_rate_exchange_list(self, mock_client, sample_funding_rate_data):
        """Test funding rate exchange list endpoint."""
        mock_client.get.return_value = sample_funding_rate_data
        
        futures = FuturesAPI(mock_client)
        funding_rates = futures.funding_rate.get_exchange_list(symbol='BTC')
        
        assert len(funding_rates) == 3
        assert funding_rates[0]['exchange'] == 'Binance'
        assert funding_rates[0]['funding_rate'] == 0.0010
        mock_client.get.assert_called_once_with(
            '/futures/funding-rate/exchange-list',
            params={'symbol': 'BTC'}
        )