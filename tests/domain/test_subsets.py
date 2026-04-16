import pytest

from anagrams.domain.subsets import all_subsets


def test_vinyl_length_3_produces_sixteen_subsets():
    result = all_subsets("VINYL", 3)
    # C(5,3) + C(5,4) + C(5,5) = 10 + 5 + 1 = 16
    assert len(result) == 16
