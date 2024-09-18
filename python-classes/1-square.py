#!/usr/bin/python3
"""Module for defining a Square class.

This module defines a Square class with a private size attribute.
"""


class Square:
    """A class that defines a square by its size.

    Attributes:
        size (int): The size of the square, not verified for type or value.

    Args:
        size (int): The size of the square.
    """
    def __init__(self, size):
        self.__size = size  # Private attribute
