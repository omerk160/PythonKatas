import unittest
from unittest.mock import patch, Mock
from katas.request_retry import request_retry  # Update the path if necessary

class TestRequestRetryL2(unittest.TestCase):
    @patch('time.sleep', return_value=None)
    @patch('katas.request_retry.requests.get')  # Mock requests.get for controlled responses
    def test_successful_request(self, mock_get, mock_sleep):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '{"Host": "httpbin.org"}'

        result = request_retry('https://httpbin.org/get')
        self.assertIn('"Host": "httpbin.org"', result)
        mock_sleep.assert_not_called()

    @patch('time.sleep', return_value=None)
    @patch('katas.request_retry.requests.get')
    def test_failed_request_with_retries(self, mock_get, mock_sleep):
        mock_get.return_value.status_code = 500  # Simulate server error
        mock_get.return_value.text = ''

        result = request_retry('https://httpbin.org/status/500', retry_limit=3)
        self.assertIsNone(result)  # Adjusted to expect None on failure
        self.assertEqual(mock_sleep.call_count, 3)

    @patch('time.sleep', return_value=None)
    @patch('katas.request_retry.requests.get')
    def test_failed_request_without_retries(self, mock_get, mock_sleep):
        mock_get.return_value.status_code = 500

        result = request_retry('https://httpbin.org/status/500', retry_limit=0)
        self.assertIsNone(result)
        mock_sleep.assert_not_called()

if __name__ == '__main__':
    unittest.main()
