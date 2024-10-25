import unittest
from python_katas.request_timeout import request_timeout


class TestRequestTimeoutL2(unittest.TestCase):

    def test_request_timeout_success(self):
        result = request_timeout('https://httpbin.org/get', timeout=5)
        self.assertIn('"Host": "httpbin.org"', result)

    def test_request_timeout_failure(self):
        result = request_timeout('https://httpbin.org/delay/5', timeout=2)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
