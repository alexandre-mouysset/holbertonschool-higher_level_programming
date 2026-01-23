#!/usr/bin/python3
"""
Module that contains a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div and returns a new matrix.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
            Each row must have the same size.
        div (int/float): The divisor. Must not be zero.

    Returns:
        list of lists of float: A new matrix with all elements divided by div
            and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of numbers,
                   or rows are not the same size,
                   or div is not a number.
        ZeroDivisionError: If div is 0.


    """
    # Check that div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check that matrix is a list
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Check that all elements are numbers
    for i in matrix:
        for value in i:
            if not isinstance(value, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of "
                    "integers/floats")

    # Check that each line is a list
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    # Check that all lines have the same size
    for i in matrix:
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    # Create a new matrix to store results
    new_matrix = []
    for i in matrix:
        new_line = []
        for value in i:
            result = round(value / div, 2)
            new_line.append(result)
        new_matrix.append(new_line)

    return new_matrix
