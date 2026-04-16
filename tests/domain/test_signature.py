import pytest

from anagrams.domain.signature import signature_of


def test_empty_string():
    assert signature_of("") == ""


def test_already_sorted():
    assert signature_of("ABCDEFG") == "ABCDEFG"


def test_lowercase_word():
    assert signature_of("vinyl") == "ILNVY"
