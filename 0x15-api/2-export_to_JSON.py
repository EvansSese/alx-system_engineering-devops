#!/usr/bin/python3
""" Script to fetch data from API """


import json
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

        employee_username = user_json.get('username')

        json_file_name = f"{employee_id}.json"
        task_list = []

        for task in todos_json:
            task_list.append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_username
            })

        data_to_export = {str(employee_id): task_list}
        with open(json_file_name, "w") as file:
            json.dump(data_to_export, file, indent=4)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    """ Run the file"""
    get_data()
