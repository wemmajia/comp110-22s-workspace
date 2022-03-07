"""Exercise 5."""

__author__ = "730395239"


def only_evens(x: list[int]) -> list[int]:
    evens: list[int] = []
    i: int = 0
    while i < len(x):
        if x[i] % 2 == 0:
            evens.append(x[i])
        i += 1
    return evens


def sub(nums: list[int], start: int, stop: int) -> list[int]:
    result: list = []
    if start < 0:
        start = 0
    if stop > len(nums):
        stop = len(nums)
    while start < stop:
        result.append(nums[start])
        start += 1
    return result


def concat(a: list[int], b: list[int]) -> list[int]:
    c: list[int] = []
    i: int = 0
    while i < len(a):
        c.append(a[i])
        i += 1
    i = 0
    while i < len(b):
        c.append(b[i])
        i += 1
    return c
