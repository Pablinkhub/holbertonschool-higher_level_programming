#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number > 0:
   print (number, "Is positive")
elif number == 0:
    print (number, "Is zero")
else:
    print (number, "is negative")
