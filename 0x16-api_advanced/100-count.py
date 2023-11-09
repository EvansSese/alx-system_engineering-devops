#!/usr/bin/python3
""" Function to return post count """
import re
import requests
import sys


def count_words(subreddit, word_list, counts=None, after=None):
    """ Function to fetch post count """
    if counts is None:
        counts = {}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': '100-count'
    }
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        try:
            # Parse the JSON response and extract the titles of the hot posts
            post_data = response.json()['data']['children']
            for post in post_data:
                title = post['data']['title']

                # Normalize the title to lowercase and remove special character
                normalized_title = re.sub(r'[^a-zA-Z0-9 ]', '',
                                          title.lower())

                # Split the normalized title into words
                words = normalized_title.split()

                # Update the counts dictionary with keyword occurrences
                for word in words:
                    if word in word_list:
                        if word in counts:
                            counts[word] += 1
                        else:
                            counts[word] = 1

            # Check if there's a 'after' key in the response,
            # indicating more pages
            after = response.json()['data']['after']
            if after is not None:
                # Recursively call the function for the next page of results
                return count_words(subreddit, word_list, counts, after)
            else:
                # Sort and print the results
                sorted_counts = sorted(counts.items(),
                                       key=lambda item: (-item[1], item[0]))
                for keyword, count in sorted_counts:
                    print(f"{keyword}: {count}")
        except (KeyError, ValueError):
            return None
    elif response.status_code == 302:
        return None
    else:
        return None


if __name__ == "__main__":
    if len(sys.argv) > 2:
        subreddit = sys.argv[2]
        word_list = sys.argv[3]
        count_words(subreddit, word_list)
