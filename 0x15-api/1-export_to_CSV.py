#!/usr/bin/python3
"""
Python script that, using this REST API, for a
given employee ID and export data in the CSV format
"""

import csv
import requests
from sys import argv

BASE_URL = 'https://jsonplaceholder.typicode.com/users/'


def get_user_name(id, name):
    """
    Retrieves the name of a user based on their ID.

    This function takes a user ID as input and returns the name of the user.

    Args:
        user_id (str): The ID of the user.

    Returns:
        str: The name of the user.
    """
    try:
        res = requests.get(f"{BASE_URL}/{id}")
        user_data = res.json()
        user_name = user_data[name]
        return user_name
    except Exception:
        print("Something went wrong :)")


def get_user_todos(id):
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
        res = requests.get(f"{BASE_URL}/{id}/todos")
        user_todos = res.json()
        return user_todos
    except Exception:
        print("Something went wrong :)")


def get_user_info():
    """
    Retrieves user information and prints completed tasks.

    This function takes a user ID as a command line argument
    and retrieves the user's name, todos, and completed todos.
    It then prints the user's name and the list of completed todos.

    Args:
        None

    Returns:
        None
    """
    if len(argv) < 2:
        return

    try:
        user_id = argv[1]
        name = get_user_name(user_id, "username")
        user_todos = get_user_todos(user_id)

        return name, user_todos, user_id

    except Exception:
        print("Something went wrong :(")


def export_to_csv():
    """
    Export user's todos to a CSV file.

    This function retrieves user information and todos
    using the `get_user_info` function, and then exports
    the todos to a CSV file named after the user's ID.

    Args:
        None

    Returns:
        None
    """
    name, user_todos, user_id = get_user_info()
    filename = f"{user_id}.csv"

    with open(filename, 'w', newline='') as csvfile:
        for todo in user_todos:
            completed = todo["completed"]
            title = todo["title"]
            csvfile.write(f'"{user_id}","{name}","{completed}","{title}"\n')


if __name__ == "__main__":
    export_to_csv()
