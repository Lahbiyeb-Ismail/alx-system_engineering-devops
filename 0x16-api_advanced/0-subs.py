#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given
subreddit. If an invalid subreddit is given, the function should return 0.
"""


import requests

BASE_URL = "https://www.reddit.com/r"


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given
    subreddit. If an invalid subreddit is given, the function should return 0.
    """
    if subreddit is None or type(subreddit) is not str:
        return 0

    headers = {"User-Agent": "Google Chrome version 88.0.4324.150"}

    url = f"{BASE_URL}/{subreddit}/about.json"

    try:
        res = requests.get(url, headers=headers)
        results = res.json()
        data = results.get("data")
        subscribers = data.get("subscribers")
        return subscribers
    except Exception:
        return 0
