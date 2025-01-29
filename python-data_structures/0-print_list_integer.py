#!/usr/bin/python3
def print_integers(lst):
    try:
        for item in lst:
            if not isinstance(item, int):
                raise ValueError("Non-integer value found")
            print("{:d}".format(item))
    except ValueError as e:
        print("Error: {0}".format(e))

