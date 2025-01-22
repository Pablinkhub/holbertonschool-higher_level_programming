#!/usr/bin/python3
for i in range (1, 100):
    print('{:02}'.format(i -1), end=', ')
    if i == 99:
        print('{:02}'.format(i), end='\n')
