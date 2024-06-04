#!/usr/bin/python3
"""
Script that queries reddit subscribers of a given subreddit.
"""


import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given
    subreddit. If an invalid subreddit is given, the function should return 0.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Chrome/81.0.4044.129"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
