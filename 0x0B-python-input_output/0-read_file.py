#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """
    Read a text file and print its contents to stdout.

    Args:
        filename (str, optional): The name
        of the text file. Defaults to an empty string.

    Returns:
        None

    Note:
        - Uses 'with' statement to open and close the file.
        - Reads the file line by line and prints each line to stdout.
        - Handles FileNotFoundError and other exceptions.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


read_file("example.txt")
