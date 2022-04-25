"""Util functions."""
from itertools import chain, combinations


def powerset(iterable):
    """powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"""
    s = list(iterable)
    response = chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

    return response


def combinations_n(iterable, n: int):
    """all combinations of N elements in iterable"""
    s = list(iterable)
    response = list(combinations(s, n))

    return response
