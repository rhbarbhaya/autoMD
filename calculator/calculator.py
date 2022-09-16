# calculator/calculator.py

"""Provide several sample math calculations.

This module allows the user to make mathematical calculations.

The module contains the following functions:

Examples:
    >>> from calculator import calculations
    >>> calculations.add(2, 4)
    6.0
    >>> calculations.multiply(2.0, 4.0)
    8.0
    >>> from calculator.calculations import divide
    >>> divide(4.0, 2)
    2.0

- `add(a, b)` - Returns the sum of two numbers.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.
"""

from typing import Union


def add(
    first: Union[int, float],
    second: Union[int, float]
) -> float:
    """Compute and return the addition of two numbers.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0
        >>> add(4.0, 2)
        6.0

    Args:
        first: A number representing the first addend in the addition.
        second: A number representing the second addend in the addition.

    Returns:
        A number representing the arithmetic sum of `first` and `second`.
    """
    return float(first + second)

def subtract(
    first: Union[int, float],
    second: Union[int, float]
) -> float:
    """Comuptes and return the difference of two numbers.

    Examples:
        >>> subtract(7.0, 3.0)
        4.0
        >>> subtract(7, 3)
        4.0
        >>> subtract(7.0, 4)
        4.0

    Args:
        first: A number representing the quantity that exists.
        second: A number representing the quantity to reduce the existing quantity by.

    Returns:
        A number representing the arithmetic difference of `first` from `second`.
    """
    return float(first - second)

def multiply(
    first: Union[int, float],
    second: Union[int, float]
) -> float:
    """Compute and return the multiplication of two numbers.

    Examples:
        >>> multiply(5.0, 3.0)
        15.0
        >>> multiply(5, 3)
        15.0
        >>> multiply(5, 3.0)
        15.0

    Args:
        first: A number representing the first number to multiply.
        second: A number representing the number to multiple the first number by.

    Returns:
        A number representing the arithmetic multiplying `first` with `second`.
    """
    return float(first * second)

def divide(
    first: Union[int, float],
    second: Union[int, float]
) -> float:
    """Compute and return the division of two numbers.

    Examples:
        >>> divide(6.0, 2.0)
        3.0
        >>> divide(6, 2)
        3.0
        >>> divide(6.0, 2)
        3.0

    Args:
        first: A number representing the divident.
        second: A number representing the divisor.

    Raises:
        ZeroDivisionError: division by zero

    Returns:
        A number representing the arithmetic division.
    """
    if second==0:
        raise ZeroDivisionError("Invalid division command")
    return float(first / second)
