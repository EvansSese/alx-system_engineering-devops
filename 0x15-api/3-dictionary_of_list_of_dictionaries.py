#!/usr/bin/python3
""" Script to fetch data from API """


import json
import requests
import sys


def get_data():
    """ Function to get data """
    url = "https://jsonplaceholder.typicode.com/"
    users_url = f"{url}users"
    try:
        users = requests.get(users_url)
        users.raise_for_status()
        users_json = users.json()

        json_file_name = "todo_all_employees.json"
        employee_data = {}

        for user in users_json:
            user_id = user.get('id')
            username = user.get('username')
            todos_url = f"{url}todos?userId={user_id}"
            todos = requests.get(todos_url)
            todos.raise_for_status()
            todos_json = todos.json()

            task_list = []
            for task in todos_json:
                task_list.append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

            employee_data[str(user_id)] = task_list
        with open(json_file_name, "w") as file:
            json.dump(employee_data, file, indent=4)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    """ Run the file"""
    get_data()
