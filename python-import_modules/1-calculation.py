#!/usr/bin/python3
from calculator_1.py import add, sub, mul, div

def main():
    
    a= 10
    b = 5
    
    print ("{} + {} = {}".format(A, b, add(a, b)))
    print ("{} + {} = {}".format(A, b, sub(a, b)))
    print ("{} + {} = {}".format(A, b, mul(a, b)))
    print ("{} + {} = {}".format(A, b, div(a, b)))

if __name__ == "__main__":
    main()
    