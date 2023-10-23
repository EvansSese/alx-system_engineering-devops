#!/usr/bin/python3
""" Script to fetch data from API """


import csv
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
        employee_id = user_json.get("id")

        csv_file_name = f"{employee_id}.csv"
        with open(csv_file_name, "w", newline="") as file:
            csv_writer = csv.writer(file, delimiter=',', quotechar='"',
                                    quoting=csv.QUOTE_ALL, lineterminator='\n')
            for task in todos_json:
                csv_writer.writerow([employee_id, employee_username,
                                     str(task.get("completed")),
                                     task.get("title")])
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    """ Run the file"""
    get_data()
