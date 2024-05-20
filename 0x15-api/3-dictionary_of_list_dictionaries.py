#!/usr/bin/python3
"""
Python script that, using this REST API, for a
given employee ID and export data in the CSV format
"""

import json
import requests

BASE_URL = 'https://jsonplaceholder.typicode.com'


def get_all_users():
    """
    Retrieves the todos of a user based on their ID.

    This function takes a user ID as input and returns a list
    of todos for that user.

    Args:
        user_id (str): The ID of the user.

    Returns:
        list: A list of todos for the user.
    """
    try:
        res = requests.get(f"{BASE_URL}/users")
        all_users = res.json()
        return all_users
    except Exception:
        print("Something went wrong :)")


def get_todos():
    """
    Retrieves the todos of a user based on their ID.

    This function takes a user ID as input and returns a list
    of todos for that user.

    Args:
        user_id (str): The ID of the user.

    Returns:
        list: A list of todos for the user.
    """
    try:
        res = requests.get(f"{BASE_URL}/todos")
        all_todos = res.json()
        return all_todos
    except Exception:
        print("Something went wrong :)")


def export_to_json():
    """
    Export user's todos to a JSON file.

    This function retrieves user information and todos
    using the `get_user_info` function, and then exports
    the todos to a JSON file named after the user's ID.

    Args:
        None

    Returns:
        None
    """
    users = get_all_users()

    users_data = {}
    for user in users:
        user_id = user["id"]
        username = user["username"]

        users_data[user_id] = []
        todos = get_todos()

        for todo in todos:
            completed = todo["completed"]
            title = todo["title"]

            users_data[user_id].append({
                "username": username,
                "task": title,
                "completed": completed,
            })

    filename = "todo_all_employees.json"

    with open(filename, 'w') as json_file:
        json.dump(users_data, json_file)


if __name__ == "__main__":
    export_to_json()
