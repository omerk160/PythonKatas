import unittest
from unittest.mock import patch
import requests  # Import requests for the timeout exception
from katas.request_timeout import request_timeout  # Update import path if necessary

class TestRequestTimeoutL2(unittest.TestCase):

    @patch('katas.request_timeout.requests.get')
    def test_request_timeout_success(self, mock_get):
        # Mock a successful response
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '{"Host": "httpbin.org"}'

        result = request_timeout('https://httpbin.org/get', timeout=5)
        self.assertIn('"Host": "httpbin.org"', result)

    @patch('katas.request_timeout.requests.get')
    def test_request_timeout_failure(self, mock_get):
        # Simulate a timeout by raising a requests.Timeout exception
        mock_get.side_effect = requests.Timeout

        result = request_timeout('https://httpbin.org/delay/5', timeout=2)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
