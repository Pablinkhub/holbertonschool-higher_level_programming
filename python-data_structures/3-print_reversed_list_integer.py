#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversed_list = my_list[::-1]
    for item in reversed_list:
        print("{0}".format(item))

my_list = [1, 2, 3, 4, 5]

print_reversed_list_integer(my_list)
