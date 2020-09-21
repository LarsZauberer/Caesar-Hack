import pytest
from caesar_hack import caesar_hack as hack


def test_hack_init():
    ha = hack("coDe", alphabet="ABC", many_char="Efj")
    assert ha.code == "code"
    assert ha.alphabet == "abc"
    assert ha.many_char == list("efj")
    assert ha.sort_counts == []
    assert ha.letters == []
    assert ha.finished == []


def test_hack_init_stupid():
    with pytest.raises(AssertionError):
        hack(2, 4, 8)
    with pytest.raises(AssertionError):
        hack("code", "ce", "e")


def test_count_and_sort():
    code = "osxwkvosxb"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    many_char = "enisratdhulcgmobwfkzpvjyxq"
    ha = hack(code, alphabet, many_char)
    ha.count_and_sort()
    assert ha.sort_counts == [('o', 2),
                              ('s', 2),
                              ('x', 2),
                              ('b', 1),
                              ('k', 1),
                              ('v', 1),
                              ('w', 1),
                              ('a', 0),
                              ('c', 0),
                              ('d', 0),
                              ('e', 0),
                              ('f', 0),
                              ('g', 0),
                              ('h', 0),
                              ('i', 0),
                              ('j', 0),
                              ('l', 0),
                              ('m', 0),
                              ('n', 0),
                              ('p', 0),
                              ('q', 0),
                              ('r', 0),
                              ('t', 0),
                              ('u', 0),
                              ('y', 0),
                              ('z', 0)]


def test_add_letters():
    code = "osxwkvosxb"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    many_char = "enisratdhulcgmobwfkzpvjyxq"
    ha = hack(code, alphabet, many_char)
    ha.count_and_sort()
    ha.add_letters()
    assert len(ha.sort_counts) == len(ha.letters)
    assert ha.finished == []


def test_calc_most_used_possibilities():
    code = "osxwkvosxb"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    many_char = "enisratdhulcgmobwfkzpvjyxq"
    ha = hack(code, alphabet, many_char)
    ha.count_and_sort()
    ha.add_letters()
    ha.calc_most_used_possibilities()
    assert ha.many_char == list("sratdhulcgmobwfkzpvjyxq")
    assert len(ha.finished) == 3


def test_key():
    code = "osxwkvosxb"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    many_char = "enisratdhulcgmobwfkzpvjyxq"
    ha = hack(code, alphabet, many_char)
    ha.count_and_sort()
    ha.add_letters()
    ha.calc_most_used_possibilities()
    assert type(ha.keys[0]) == int
    assert type(ha.key) == int
