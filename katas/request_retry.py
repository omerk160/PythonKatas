import requests
import time


def request_retry(url, retry_limit=3):
    """
    Performs a GET request to the given URL with retry logic for server errors (status code >= 500).
    Retries up to `retry_limit` times with a 3-second delay between attempts.

    :param url: str - A valid URL
    :param retry_limit: int - Maximum number of retries
    :return: str - Response text if the request is successful, None if all attempts fail
    """
    attempts = 0

    while attempts <= retry_limit:
        try:
            # Perform the GET request
            response = requests.get(url)

            # Check if the response is a server error
            if response.status_code >= 500:
                print(f"Attempt {attempts + 1}: Server error (status {response.status_code}), retrying...")
                attempts += 1
                if attempts <= retry_limit:
                    time.sleep(3)
            else:
                # Return the response text if the request is successful
                return response.text

        except requests.RequestException as e:
            print(f"Attempt {attempts + 1}: Request failed with error: {e}")
            attempts += 1
            if attempts <= retry_limit:
                time.sleep(3)

    # If all attempts fail, return None
    print("All attempts failed.")
    return None


if __name__ == '__main__':
    print(request_retry('https://www.google.com'))
    print(request_retry('https://sdfsgewcwe4rc34rxwrfxw3r3xrxr.com'))
