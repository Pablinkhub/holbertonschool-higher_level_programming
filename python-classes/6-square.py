#!/usr/bin/python3
"""Defines a Square with size, area methods, and position handling."""


class Square:
    """Class for squares with size validation and graphical positioning."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize with optional size and position; both validated."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve size of square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with integer and non-negative check."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve position of square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position with tuple of 2 positive ints check."""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return area of square."""
        return self.__size ** 2

    def my_print(self):
        """Print square with '#' character and handle positioning."""
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end='')
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
