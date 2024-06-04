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
    user_agent = {"User-Agent": "api_advanced-project"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {"limit": 10}
    results = requests.get(
        url, params=parameters, headers=user_agent, allow_redirects=False
    )

    if results.status_code == 200:
        my_data = results.json().get("data").get("children")

        for i in my_data:
            print(i.get("data").get("title"))
    else:
        print("None")
