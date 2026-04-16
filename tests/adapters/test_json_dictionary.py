import json

import pytest

from anagrams.adapters.json_dictionary import JsonDictionaryAdapter


@pytest.fixture
def sigmap_file(tmp_path):
    data = {
        "EILNST": ["ENLIST", "LISTEN", "SILENT", "TINSEL"],
        "ILNVY": ["VINYL"],
    }
    path = tmp_path / "sigmap.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    return path


def test_lookup_found(sigmap_file):
    adapter = JsonDictionaryAdapter(path=sigmap_file)
    assert sorted(adapter.lookup("EILNST")) == ["ENLIST", "LISTEN", "SILENT", "TINSEL"]


def test_lookup_not_found(sigmap_file):
    adapter = JsonDictionaryAdapter(path=sigmap_file)
    assert adapter.lookup("ZZZZZ") == []
