#!/usr/bin/python3

"""
Script that prints the titles of the
first 10 hot posts listed for a given
subreddit
"""

from requests import get


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {"User-agent": "Google Chrome Version 81.0.4044.129"}

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {"limit": 10}

    response = get(url, headers=user_agent, params=params)
    results = response.json()

    try:
        posts = results.get("data").get("children")

        for post in posts:
            print(post.get("data").get("title"))

    except Exception:
        print("None")
