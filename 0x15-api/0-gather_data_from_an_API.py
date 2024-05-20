#!/usr/bin/python3
"""
Python script that, using this REST API, for a
given employee ID, returns information about his/her
TODO list progress.
"""

import requests
from sys import argv

BASE_URL = 'https://jsonplaceholder.typicode.com/users/'


def get_user_name(id):
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
        user_name = user_data["name"]
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


def get_completed_todos(todos):
    """
    Retrieves the completed todos from a list of todos.

    This function takes a list of todos and returns a new
    list containing only the completed todos.

    Args:
        user_todos (list): A list of todos.

    Returns:
        list: A list of completed todos.
    """
    completed_todos = []

    for todo in todos:
        if (todo["completed"]):
            completed_todos.append(todo)

    return completed_todos


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
        name = get_user_name(user_id)
        user_todos = get_user_todos(user_id)
        todos_num = len(user_todos)
        done_todos = 0

        for todo in user_todos:
            if todo["completed"]:
                done_todos += 1

        print(f"Employee {name} is done with tasks({done_todos}/{todos_num}):")

        completed_todos = get_completed_todos(user_todos)

        if (len(completed_todos) > 0):
            for todo in completed_todos:
                todo_title = todo["title"]
                print(f"\t {todo_title}")
    except Exception:
        print("Something went wrong :(")


if __name__ == "__main__":
    get_user_info()
