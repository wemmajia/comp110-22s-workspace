import pytest
from dictionary import invert, count, favorite_color


def test_invert() -> None:
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_invert_2() -> None:
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_3() -> None:
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}
