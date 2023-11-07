#!/usr/bin/python3
""" Function to return top ten posts """
import requests
import sys


def top_ten(subreddit):
    """ Function to fetch top ten posts """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': '1-top_ten'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            post_data = response.json()['data']['children'][:10]
            for post in post_data:
                title = post['data']['title']
                print(f"{title}")
        except (KeyError, ValueError):
            print(None)
    else:
        print(None)


if __name__ == "__main__":
    if len(sys.argv) > 2:
        subreddit = sys.argv[2]
        top_ten(subreddit)
