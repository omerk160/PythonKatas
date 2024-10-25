import requests


def reviewed_pull_requests(repo_url):
    """
    The function receives a GitHub repo HTTP URL (can be ended with .git or without), and returns
    all Pull Requests in this repo that have been reviewed in the last 10 days.

    The function returns list of PR urls.

    You can use `requests` to list repository events from GitHub API: https://docs.github.com/en/rest/activity/events?apiVersion=2022-11-28
    In the events, search for a 'PullRequestReviewEvent' event.

    :param repo_url: str
    :return: list of str
    """
    return None


if __name__ == '__main__':
    print(reviewed_pull_requests('https://github.com/redis/redis.git'))

