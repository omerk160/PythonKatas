import requests
from datetime import datetime, timedelta


def reviewed_pull_requests(repo_url):
    """
    The function receives a GitHub repo HTTP URL (can be ended with .git or without), and returns
    all Pull Requests in this repo that have been reviewed in the last 10 days.

    The function returns a list of PR urls.

    :param repo_url: str
    :return: list of str
    """
    # Normalize the repo_url to extract owner and repo name
    if repo_url.endswith('.git'):
        repo_url = repo_url[:-4]  # Remove .git suffix
    # Convert URL to the format "owner/repo"
    repo_name = repo_url.split('github.com/')[-1]

    # Prepare GitHub API URL for events
    events_url = f'https://api.github.com/repos/{repo_name}/events'

    # Perform the GET request to the GitHub API
    response = requests.get(events_url)

    # Debugging: Check if the request was successful
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return []  # Return an empty list if the request fails

    events = response.json()
    print(f"Retrieved {len(events)} events.")  # Debugging: Number of events fetched
    ten_days_ago = datetime.utcnow() - timedelta(days=10)
    reviewed_pr_urls = []

    for event in events:
        # Debugging: Print event type and created_at for inspection
        print(f"Event type: {event['type']}, Created at: {event['created_at']}")

        # Check for 'PullRequestReviewEvent'
        if event['type'] == 'PullRequestReviewEvent':
            # Get the PR URL
            pr_url = event['payload']['pull_request']['html_url']
            # Get the review date
            review_date = datetime.strptime(event['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            # Check if the review date is within the last 10 days
            if review_date >= ten_days_ago:
                reviewed_pr_urls.append(pr_url)

    return reviewed_pr_urls


if __name__ == '__main__':
    print(reviewed_pull_requests('https://github.com/redis/redis.git'))
