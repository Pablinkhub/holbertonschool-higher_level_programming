#!/usr/bin/python3
"""Defines a Square class, the square."""


class Square:
    """Class for area calculation and graphical representation."""
    
    def __init__(self, size=0):
        """Initialize a Square with optional size, defaults to 0"""
        self.size = size  # Utiliza el setter para validar

    @property
    def size(self):
        """Return the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with integer and non-negative validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using # or an empty line if size is 0."""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
