"""
Tests for the CoinGlass client
"""
import pytest
from unittest.mock import Mock, patch, MagicMock
import requests
from coinglass import CoinGlassClient, CoinGlassAPIError


class TestCoinGlassClient:
    """Test CoinGlassClient class."""
    
    def test_client_initialization_with_api_key(self):
        """Test client initialization with API key."""
        client = CoinGlassClient(api_key='test_key')
        assert client.api_key == 'test_key'
        assert client.base_url == 'https://open-api-v4.coinglass.com/api'
    
    def test_client_initialization_from_env(self, monkeypatch):
        """Test client initialization from environment variable."""
        monkeypatch.setenv('CG_API_KEY', 'env_test_key')
        client = CoinGlassClient()
        assert client.api_key == 'env_test_key'
    
    def test_client_initialization_no_key(self):
        """Test client initialization without API key raises error."""
        with pytest.raises(ValueError, match="API key is required"):
            CoinGlassClient(api_key=None)
    
    @patch('requests.Session.request')
    def test_get_request(self, mock_request):
        """Test GET request method."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'code': '0', 'msg': 'success', 'data': ['BTC', 'ETH']}
        mock_request.return_value = mock_response
        
        client = CoinGlassClient(api_key='test_key')
        result = client.get('/futures/supported-coins')
        
        assert result['code'] == '0'
        assert result['data'] == ['BTC', 'ETH']
        mock_request.assert_called_once()
    
    @patch('requests.Session.request')
    def test_api_error_response(self, mock_request):
        """Test handling of API error response."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'code': '401', 'msg': 'Unauthorized'}
        mock_request.return_value = mock_response
        
        client = CoinGlassClient(api_key='test_key')
        
        with pytest.raises(CoinGlassAPIError) as exc_info:
            client.get('/futures/supported-coins')
        
        assert exc_info.value.code == '401'
        assert 'Unauthorized' in str(exc_info.value)
    
    @patch('requests.Session.request')
    def test_rate_limiting(self, mock_request):
        """Test rate limiting handling."""
        # First response: rate limited
        mock_response_429 = Mock()
        mock_response_429.status_code = 429
        mock_response_429.headers = {'Retry-After': '1'}
        
        # Second response: success
        mock_response_200 = Mock()
        mock_response_200.status_code = 200
        mock_response_200.json.return_value = {'code': '0', 'msg': 'success', 'data': []}
        
        mock_request.side_effect = [mock_response_429, mock_response_200]
        
        client = CoinGlassClient(api_key='test_key')
        
        with patch('time.sleep') as mock_sleep:
            result = client.get('/test-endpoint')
            assert result['code'] == '0'
            mock_sleep.assert_called_once_with(1)
    
    @patch('requests.Session.request')
    def test_request_with_params(self, mock_request):
        """Test request with query parameters."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'code': '0', 'msg': 'success', 'data': {}}
        mock_request.return_value = mock_response
        
        client = CoinGlassClient(api_key='test_key')
        params = {'symbol': 'BTC', 'interval': '1h'}
        result = client.get('/futures/price/history', params=params)
        
        # Check that params were passed
        call_args = mock_request.call_args
        assert call_args[1]['params'] == params
    
    def test_context_manager(self):
        """Test client as context manager."""
        with CoinGlassClient(api_key='test_key') as client:
            assert client.api_key == 'test_key'
        # Should not raise any errors on exit
    
    @patch('requests.Session.request')
    def test_json_decode_error(self, mock_request):
        """Test handling of invalid JSON response."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.side_effect = requests.exceptions.JSONDecodeError('Invalid', '', 0)
        mock_response.text = 'Invalid JSON'
        mock_request.return_value = mock_response
        
        client = CoinGlassClient(api_key='test_key')
        
        with pytest.raises(CoinGlassAPIError) as exc_info:
            client.get('/test-endpoint')
        
        assert 'Invalid JSON' in str(exc_info.value)