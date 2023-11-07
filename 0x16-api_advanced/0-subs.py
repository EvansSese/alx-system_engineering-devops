#!/usr/bin/python3
""" Function to return number of subscribers """
import requests
import sys


def number_of_subscribers(subreddit):
    """ Function to fetch subs """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': '0-subs'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            subreddit_data = response.json()['data']
            subscribers = subreddit_data['subscribers']
            return subscribers
        except (KeyError, ValueError):
            return 0
    else:
        return 0


if __name__ == "__main__":
    if len(sys.argv) > 2:
        subreddit = sys.argv[2]
        number_of_subscribers(subreddit)
