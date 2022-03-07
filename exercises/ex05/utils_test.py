"""Exercise 5 test."""

__author__ = "730395239"

from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    assert only_evens([]) == []


def test_only_evens_none() -> None:
    assert only_evens([1, 3, 5, 7]) == []


def test_only_evens() -> None:
    assert only_evens([0, 2, 3, 4, 5, 6, 7]) == [0, 2, 4, 6]


def test_sub_empty() -> None:
    assert sub([], 5, 9) == []


def test_sub() -> None:
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_sub_2() -> None:
    assert sub([-5, 0, 1, 4], -7, 4) == [-5, 0, 1, 4]


def test_concat_empty() -> None:
    assert concat([], [1]) == [1]


def test_concat() -> None:
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_concat_2() -> None:
    assert concat([0], []) == [0]