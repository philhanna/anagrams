"""Application service for anagram search.

This module contains the single use-case of the application: given a word and
an optional minimum length, find every dictionary word that can be formed from
some subset of the input word's letters.
"""

from argparse import Namespace

from anagrams.domain.signature import signature_of
from anagrams.domain.subsets import all_subsets
from anagrams.ports.dictionary_port import DictionaryPort


class SearchService:
    """Application service: finds all dictionary words that are anagrams of
    any subset of the input word.

    The service is stateless beyond the injected dictionary.  It can be
    constructed once and reused for multiple searches.

    Parameters
    ----------
    dictionary:
        A ``DictionaryPort`` implementation used to look up words by
        signature.  Typically a ``JsonDictionaryAdapter``, but any conforming
        implementation is accepted.
    """

    def __init__(self, dictionary: DictionaryPort) -> None:
        """Initialise the service with a dictionary port.

        Parameters
        ----------
        dictionary:
            The secondary port used to resolve signatures to word lists.
        """
        self._dictionary = dictionary

    def search(self, args: Namespace, length: int = 3) -> list[str]:
        """Find all dictionary words that are anagrams of any subset of *word*.

        The algorithm:

        1. Convert *word* to uppercase.
        2. Enumerate every non-empty subset of its characters whose length is
           at least *length*.
        3. Compute the signature of each subset.
        4. Query the dictionary for matching words.
        5. Collect unique matches and return them in sorted order.

        Parameters
        ----------
        word:
            The input word whose letter pool will be searched.  Case is
            ignored — ``"Triangle"`` and ``"TRIANGLE"`` produce the same
            results.
        length:
            Minimum number of characters a result word must have.  Defaults
            to ``3`` to filter out very short words.

        Returns
        -------
        list[str]
            Lexicographically sorted list of unique matching words, all in
            the case returned by the dictionary (typically uppercase).
        """
        word = args.word
        subsets = all_subsets(word.upper(), length)
        found: set[str] = set()
        for subset in subsets:
            sig = signature_of(subset)
            found.update(self._dictionary.lookup(sig))
        return sorted(found)
