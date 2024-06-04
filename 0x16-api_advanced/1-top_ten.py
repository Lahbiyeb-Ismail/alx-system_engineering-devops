#!/usr/bin/python3

"""
Script that prints the titles of the first 10 hot posts
listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = {"user-agent": "Mozilla/5.0"}
    params = {"limit": 10}

    response = requests.get(
        url,
        params=params,
        allow_redirects=False,
        headers=user_agent,
    )

    if response.status_code == 200:
        posts = response.json().get("data").get("children")

        for post in posts:
            post_title = post.get("data").get("title")
            print(post_title)
    else:
        print("None")
