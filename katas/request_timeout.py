import requests


def request_timeout(url, timeout=5):
    """
    Performs a GET request to the given URL with a specified timeout.
    Returns the response text if successful, or None if a timeout occurs.

    :param url: str - A valid URL
    :param timeout: int - Timeout duration in seconds
    :return: str - Response text or None if a timeout occurs
    """
    try:
        # Perform the GET request with the specified timeout
        response = requests.get(url, timeout=timeout)

        # Return response text if successful
        return response.text

    except requests.Timeout:
        # Return None in case of a timeout
        print("Request timed out.")
        return None

    except requests.RequestException as e:
        # Catch other possible exceptions and print them
        print(f"Request failed with error: {e}")
        return None


if __name__ == '__main__':
    print(request_timeout('https://www.google.com'))
    print(request_timeout('https://httpbin.org/delay/5', timeout=3))
