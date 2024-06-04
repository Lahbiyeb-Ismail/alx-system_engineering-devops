#!/usr/bin/python3

import requests

BASE_URL = "https://www.reddit.com/r"


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function
    should return None.
    """
    headers = {"User-Agent": "api_advanced-project"}

    url = "{}/{}/hot.json".format(BASE_URL, subreddit)

    if after:
        url += "?after={}".format(after)

    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return None

    try:
        results = res.json()
        data = results.get("data")
        after = data.get("after")
        children = data.get("children")

        for child in children:
            hot_list.append(child.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    except Exception:
        return None
