#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given
subreddit. If an invalid subreddit is given, the function should return 0.
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

    BASE_URL = "https://www.reddit.com/r"

    headers = {"User-Agent": "Google Chrome Version 125.0.6422.142"}

    url = "{}/{}/about.json".format(BASE_URL, subreddit)

    try:
        res = requests.get(url, headers=headers)
        results = res.json()
        data = results.get("data")
        subscribers = data.get("subscribers")

        if subscribers is None:
            return 0

        return subscribers
    except Exception:
        return 0
