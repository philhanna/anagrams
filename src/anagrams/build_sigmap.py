"""Build sigmap.json from a word list.

Usage:
    python -m anagrams.build_sigmap [WORDS_FILE] > sigmap.json

Reads words from WORDS_FILE (default: setup/words.txt relative to the
project root), groups them by signature, and writes the JSON map to stdout.
"""

import json
import sys
from pathlib import Path

from anagrams.domain.signature import signature_of

_DEFAULT_WORDS = Path(__file__).parent.parent.parent.parent / "setup" / "words.txt"


def build(words_path: Path) -> dict[str, list[str]]:
    """Read *words_path* and build a signature → word-list mapping.

    Each non-empty line is treated as one word.  Words are uppercased before
    being stored so that dictionary lookups are case-insensitive.

    Parameters
    ----------
    words_path:
        Path to a plain-text word list with one word per line.  Lines that
        are blank after stripping whitespace are skipped.  Encoding errors are
        silently ignored so that files with mixed or non-UTF-8 bytes do not
        abort the build.

    Returns
    -------
    dict[str, list[str]]
        A mapping from signature to list of uppercased words, suitable for
        direct serialisation to ``sigmap.json``.

    Examples
    --------
    Given a word list containing ``listen`` and ``silent``:

    >>> build(path)["EILNST"]
    ['LISTEN', 'SILENT']
    """
    sigmap: dict[str, list[str]] = {}
    with words_path.open(encoding="utf-8", errors="ignore") as fh:
        for line in fh:
            word = line.strip().upper()
            if word:
                sig = signature_of(word)
                sigmap.setdefault(sig, []).append(word)
    return sigmap


def main() -> None:
    """CLI entry point: build and print the signature map as JSON.

    Reads the word list from the path given as the first positional argument,
    or from ``setup/words.txt`` (relative to the project root) if no argument
    is supplied.  The resulting JSON object is written to *stdout* with no
    trailing newline, making it suitable for shell redirection:

    .. code-block:: bash

        python -m anagrams.build_sigmap > src/anagrams/data/sigmap.json
        python -m anagrams.build_sigmap /path/to/words.txt > custom.json
    """
    words_path = Path(sys.argv[1]) if len(sys.argv) > 1 else _DEFAULT_WORDS
    sigmap = build(words_path)
    json.dump(sigmap, sys.stdout)


if __name__ == "__main__":
    main()
