import json

import pytest

from anagrams.adapters.json_dictionary import JsonDictionaryAdapter
from anagrams.application.search_service import SearchService


@pytest.fixture
def service(tmp_path):
    data = {
        "AELRT": ["ALTER", "ALERT", "RATEL"],
        "AEL": ["ALE", "LEA"],
        "AER": ["ARE", "EAR", "ERA"],
        "ELT": ["LET"],
    }
    path = tmp_path / "sigmap.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    return SearchService(JsonDictionaryAdapter(path=path))


def test_search_returns_sorted_unique_words(service):
    results = service.search("LATER", 3)
    assert results == sorted({"ALTER", "ALERT", "RATEL", "ALE", "LEA", "ARE", "EAR", "ERA", "LET"})


def test_search_full_length_filters_short_words(service):
    results = service.search("LATER", 5)
    assert "ALTER" in results
    assert "ALE" not in results


def test_search_is_case_insensitive(service):
    lower = service.search("later", 3)
    upper = service.search("LATER", 3)
    assert lower == upper
