#!/usr/bin/python3
for i in range (0, 100):
    if i in range (99, 100):
        print('{:02}'.format(i), end='')
    else:
        print('{:02}'.format(i - 1), end=', ')
