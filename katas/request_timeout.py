import requests


def request_timeout(url, timeout=5):
    """
    The function performs a GET request to the given url, while implementing a timeout logic, waiting `timeout` seconds before terminating the request.

    In a case of timeout, return None.

    :param url: a valid url
    :param timeout: int
    :return: Return the resulting response as text or None.
    """
    return None


if __name__ == '__main__':
    print(request_timeout('google.com'))
    print(request_timeout('https://httpbin.org/delay/5', timeout=3))

