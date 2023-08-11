#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    args = sys.argv[1:]

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print(f"1 argument:")
        print(f"1: {args[0]}")
    else:
        print(f"{num_args} arguments:")
        for i, arg in enumerate(args, start=1):
            print(f"{i}: {arg}")
