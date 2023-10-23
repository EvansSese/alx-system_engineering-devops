#!/usr/bin/python3
""" Script to fetch data from API """


import requests
import sys


def get_data():
    """ Function to get data """
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    users_url = f"{url}users/{employee_id}"
    todos_url = f"{url}todos?userId={employee_id}"
    try:
        user = requests.get(users_url)
        user.raise_for_status()
        user_json = user.json()

        todos = requests.get(todos_url)
        todos.raise_for_status()
        todos_json = todos.json()

        employee_name = user_json["name"]
        total_tasks = len(todos_json)
        completed_tasks = sum(1 for task in todos_json if task["completed"])

        print(f"Employee {employee_name} is done with tasks({completed_tasks}"
              f"/{total_tasks}):")
        for completed_task in todos_json:
            if completed_task["completed"]:
                print(f"\t{completed_task['title']}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    """ Run the file"""
    get_data()
