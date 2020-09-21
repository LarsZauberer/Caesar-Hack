from caesar_code import caesar_code
import pytest


def test_caesar_encrypt_normal():
    assert caesar_code("ABC", 1, "abcdefghijklmnopqrstuvwxyz").encrypt() == "BCD"
    assert caesar_code("abc", 1, "abcdefghijklmnopqrstuvwxyz").encrypt() == "BCD"
    assert type(caesar_code("ABC", 1, "abcdefghijklmnopqrstuvwxyz").encrypt()) == str


def test_caesar_encrypt_stupid():
    with pytest.raises(AssertionError):
        caesar_code(2, 2, "abcdefghijklmnopqrstuvwxyz").encrypt() == None
        caesar_code(None, None, "abcdefghijklmnopqrstuvwxyz").encrypt() == None
        caesar_code("Hallo", "Test", "abcdefghijklmnopqrstuvwxyz").encrypt() == None


def test_caesar_encrypt_key_test():
    assert caesar_code("ABC", 2, "abcdefghijklmnopqrstuvwxyz").encrypt() == "CDE"


def test_caesar_decrypt_normal():
    assert caesar_code("CDE", 2, "abcdefghijklmnopqrstuvwxyz").decrypt() == "ABC"
    assert caesar_code("BCD", 1, "abcdefghijklmnopqrstuvwxyz").decrypt() == "ABC"
    assert type(caesar_code("CDE", 1, "abcdefghijklmnopqrstuvwxyz").decrypt()) == str
