"""JSON-backed implementation of the dictionary secondary port.

The adapter reads a prebuilt ``sigmap.json`` file — a JSON object whose keys
are word signatures (sorted uppercase letters) and whose values are lists of
matching words.  The entire map is loaded into memory on construction and
kept for the lifetime of the adapter, making individual ``lookup`` calls O(1).
"""

import json
from importlib.resources import files as resource_files
from pathlib import Path

from anagrams.ports.dictionary_port import DictionaryPort


class JsonDictionaryAdapter(DictionaryPort):
    """Secondary adapter: loads the signature map from a JSON file.

    On construction the JSON file is parsed once into an in-memory dictionary.
    Subsequent ``lookup`` calls are pure hash-table lookups with no further
    I/O.

    Parameters
    ----------
    path:
        Path to a ``sigmap.json`` file.  When ``None`` (the default) the
        adapter loads the file bundled inside the ``anagrams.data`` package,
        which is the normal production path.  Supply an explicit path to use
        a custom word list or for testing.
    """

    def __init__(self, path: str | Path | None = None) -> None:
        """Load and parse the signature map.

        Parameters
        ----------
        path:
            Filesystem path to a ``sigmap.json`` file, or ``None`` to use the
            bundled data file.

        Raises
        ------
        FileNotFoundError
            If *path* is provided but does not exist.
        json.JSONDecodeError
            If the file at *path* is not valid JSON.
        """
        if path is None:
            text = resource_files("anagrams.data").joinpath("sigmap.json").read_text(
                encoding="utf-8"
            )
        else:
            text = Path(path).read_text(encoding="utf-8")
        self._sigmap: dict[str, list[str]] = json.loads(text)

    def lookup(self, signature: str) -> list[str]:
        """Return all words in the dictionary whose signature equals *signature*.

        Parameters
        ----------
        signature:
            A canonical word signature — sorted uppercase letters (e.g.
            ``"EILNST"``).

        Returns
        -------
        list[str]
            Matching words, or an empty list if none are found.
        """
        return self._sigmap.get(signature, [])
