from letter import letter
from caesar_hack import caesar_hack as hack
import pytest


def test_letter_init():
    code = "osxwkvosxb"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    many_char = "enisratdhulcgmobwfkzpvjyxq"
    ha = hack(code, alphabet, many_char)
    char = letter('c', ha)
    assert char.char == 'c'
    assert type(char.hack) == hack


def test_letter_init_stupid():
    with pytest.raises(AssertionError):
        letter(8, hack("", "", ""))
        letter('a', 8)


def test_letter_add_possibilities():
    code = "osxwkvosxb"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    many_char = "enisratdhulcgmobwfkzpvjyxq"
    ha = hack(code, alphabet, many_char)
    char = letter('c', ha)
    char.add_possibilities(3)
    assert len(char.possibilities) == 3
    code = "osxwkvosxb"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    many_char = "enisratdhulcgmobwfkzpvjyxq"
    ha = hack(code, alphabet, many_char)
    char = letter('d', ha)
    char.add_possibilities(5)
    assert len(char.possibilities) == 5


def test_letter_add_possibilities_stupid():
    code = "osxwkvosxb"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    many_char = "enisratdhulcgmobwfkzpvjyxq"
    ha = hack(code, alphabet, many_char)
    char = letter('c', ha)
    with pytest.raises(AssertionError):
        char.add_possibilities("a")


def test_letter_add_key_possibilities():
    code = "osxwkvosxb"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    many_char = "enisratdhulcgmobwfkzpvjyxq"
    ha = hack(code, alphabet, many_char)
    char = letter('c', ha)
    char.add_possibilities(3)
    char.add_key_possibilities()
    assert len(char.key_possibilities) == 3


def test_get_index():
    code = "osxwkvosxb"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    many_char = "enisratdhulcgmobwfkzpvjyxq"
    ha = hack(code, alphabet, many_char)
    char = letter('c', ha)
    assert char.get_index("a") == 0
    assert char.get_index("b") == 1
