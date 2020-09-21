from letter import letter
from caesar_hack import caesar_hack
import pytest


def letter_init_test():
    char = letter('c', caesar_hack())
    assert char.char == 'c'
    assert type(char.hack) == caesar_hack


def letter_init_stupid_test():
    with pytest.raises(AssertionError):
        letter(8, caesar_hack())
        letter('a', 8)


def letter_add_possibilities_test():
    char = letter('c', caesar_hack())
    char.add_possibilities(3)
    assert len(char.add_possibilities) == 3
    char = letter('d', caesar_hack())
    char.add_possibilities(5)
    assert len(char.add_possibilities) == 5


def letter_add_possibilities_stupid_test():
    char = letter('c', caesar_hack())
    with pytest.raises(AssertionError):
        char.add_possibilities(3)


def letter_add_key_possibilities_test():
    char = letter('c', caesar_hack())
    char.add_possibilities(3)
    char.add_key_possibilities()
    assert len(char.add_key_possibilities) == 3
