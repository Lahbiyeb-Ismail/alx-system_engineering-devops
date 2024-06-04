#!/usr/bin/python3
""""
Function that queries the Reddit API and returns the number of
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
    if subreddit is None:
        return 0

    headers = {"User-Agent": "Chrome/88.0.4324.150"}

    url = "{}/{}/about.json".format(BASE_URL, subreddit)

    try:
        res = requests.get(url, headers=headers, allow_redirects=False)
        results = res.json()
        data = results.get("data")
        subscribers = data.get("subscribers")

        return subscribers
    except Exception:
        return 0
