import requests


def request_retry(url, retry_limit=3):
    """
    The function performs a GET request to the given url, while implementing a linear retry logic, sleeping 3 seconds between every try.
    Failed request is defined by status code >= 500.
    The function stops after retry_limit retries (if retry_limit=3, there should be 4 attempts in total. The first one, and 3 more retries).

    :param url: a valid url
    :param retry_limit: int
    :return: Return the resulting response as text.
    """
    return None


if __name__ == '__main__':
    print(request_retry('google.com'))
    print(request_retry('sdfsgewcwe4rc34rxwrfxw3r3xrxr.com'))

