import pytest

from anagrams.domain.permutations import permutations


def test_abc_produces_six_permutations():
    result = permutations("ABC")
    assert len(result) == 6
    assert sorted(result) == ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
