"""Secondary port interface for dictionary (word-lookup) operations.

Any class that satisfies this interface can be injected into the application
layer as the backing word store, making it straightforward to swap the data
source (e.g. JSON file, database, in-memory list) without touching business
logic.
"""

from abc import ABC, abstractmethod


class DictionaryPort(ABC):
    """Secondary port: defines how the application accesses word lookup by signature.

    Implementors must be safe to construct once and query many times.  The
    ``lookup`` method must be pure — given the same signature it must always
    return the same list.
    """

    @abstractmethod
    def lookup(self, signature: str) -> list[str]:
        """Return all words whose signature equals *signature*.

        Parameters
        ----------
        signature:
            A canonical word signature as produced by
            ``anagrams.domain.signature.signature_of`` — sorted uppercase
            letters of a word (e.g. ``"EILNST"``).

        Returns
        -------
        list[str]
            Every word in the dictionary whose sorted-uppercase letters match
            *signature*, or an empty list if none exist.
        """
