import unittest
from unittest.mock import patch
from python_katas.request_retry import request_retry


class TestRequestRetryL2(unittest.TestCase):
    @patch('time.sleep', return_value=None)
    def test_successful_request(self, mock_sleep):
        result = request_retry('https://httpbin.org/get')
        self.assertIn('"Host": "httpbin.org"', result)
        mock_sleep.assert_not_called()

    @patch('time.sleep', return_value=None)
    def test_failed_request_with_retries(self, mock_sleep):
        result = request_retry('https://httpbin.org/status/500', retry_limit=3)
        self.assertEqual(result, '')
        self.assertEqual(mock_sleep.call_count, 3)

    @patch('time.sleep', return_value=None)
    def test_failed_request_without_retries(self, mock_sleep):
        result = request_retry('https://httpbin.org/status/500', retry_limit=0)
        self.assertEqual(result, '')
        mock_sleep.assert_not_called()


if __name__ == '__main__':
    unittest.main()
