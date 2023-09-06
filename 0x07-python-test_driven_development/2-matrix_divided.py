#!/usr/bin/python3

"""Defines an matrix divided function."""


def matrix_divided(matrix, div):
    """
    Divide each element of a matrix by a divisor.

    Args:
        matrix (list): A matrix (list of lists) of integers or floats.
        div (int or float): The divisor.

    Returns:
        list: A new matrix with the elements divided by the divisor,
              rounded to two decimal places.

    Raises:
        TypeError: If the matrix is not a valid matrix (list of lists)
                   of integers/floats, or if each row of the matrix
                   does not have the same size.
        ZeroDivisionError: If the divisor is zero.

    """
    if not isinstance(matrix, list) or any(
        [not isinstance(lst, list) for lst in matrix]
        ) or [not isinstance(number, (int, float))
              for number in
              [num for lst in matrix for num in lst]]:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(lst) for lst in matrix)) == 1:
        raise TypeError(
            "Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("div must be a non-zero number")
    return [[round(number, 2) for number in row]
            for row in matrix]
