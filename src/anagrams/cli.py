"""Primary adapter: command-line interface for the anagrams search service."""

import argparse
import sys

from anagrams.adapters.json_dictionary import JsonDictionaryAdapter
from anagrams.application.search_service import SearchService


def main() -> None:
    """Entry point for the ``anagrams`` command-line tool.

    Parses command-line arguments, constructs the application stack
    (``JsonDictionaryAdapter`` → ``SearchService``), runs the search, and
    prints each result word on its own line.

    Command-line interface
    ----------------------
    .. code-block:: text

        usage: anagrams [-h] [-n NUM] [-f] [word]

        positional arguments:
          word               input word

        options:
          -h, --help         show this help message and exit
          -n NUM, --length NUM
                             limits output to words of length >= NUM (default=3)
          -f, --full         include only words the same length as the input

    Exit codes
    ----------
    0
        One or more results printed successfully (or zero results found —
        finding no matches is not an error).
    1
        No word argument supplied, or an unexpected exception was raised.
    """
    parser = argparse.ArgumentParser(
        prog="anagrams",
        description="Finds anagrams of all subsets of the specified word of sufficient length.",
    )
    parser.add_argument("word", nargs="?", help="input word")
    parser.add_argument(
        "-n",
        "--length",
        type=int,
        default=3,
        metavar="NUM",
        help="limits output to words of length >= NUM (default=3)",
    )
    parser.add_argument(
        "-f",
        "--full",
        action="store_true",
        help="include only words the same length as the input",
    )
    parser.add_argument(
        "-w",
        "--word-lengths",
        action="store_true",
        help="append word length in parentheses"
    )

    args = parser.parse_args()

    if args.word is None:
        parser.print_usage(sys.stderr)
        sys.exit(1)

    length = len(args.word) if args.full else args.length

    try:
        dictionary = JsonDictionaryAdapter()
        service = SearchService(dictionary)
        results = service.search(args, length)
        for word in results:
            print(word)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
