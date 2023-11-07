#!/usr/bin/python3
""" Function to return top ten posts """
import requests
import sys


def recurse(subreddit, hot_list=None, after=None):
    """ Function to fetch top ten posts """
    if hot_list is None:
        hot_list = []
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': '2-recurse'
    }
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        try:
            post_data = response.json()['data']['children'][:10]
            for post in post_data:
                title = post['data']['title']
                hot_list.append(title)
            after = response.json()['data']['after']
            if after is not None:
                # Recursively call the function for the next page of results
                return recurse(subreddit, hot_list, after)
            else:
                # No more pages, return the hot_list
                return hot_list
        except (KeyError, ValueError):
            return None
    elif response.status_code == 302:
        return None
    else:
        return None


if __name__ == "__main__":
    if len(sys.argv) > 2:
        subreddit = sys.argv[2]
        recurse(subreddit)
