"""Numbers module."""
from typing import List


def sum_even_numbers(numbers: List[int]) -> int:
    """Sum of all evem numbers.

    Given a list of integers, return the sum of all even numbers in the list.
    """
    return sum(num for num in numbers if num % 2 == 0)
