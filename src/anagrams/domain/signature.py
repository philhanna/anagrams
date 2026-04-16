"""Canonical signature computation for anagram detection.

Two words are anagrams of each other if and only if they share the same
signature (the multiset of their letters, represented here as a sorted
uppercase string).  For example, ``"listen"`` and ``"silent"`` both produce
the signature ``"EILNST"``.
"""


def signature_of(word: str) -> str:
    """Return the canonical signature of *word*.

    The signature is formed by converting all letters to uppercase and sorting
    them.  Two words with the same signature are anagrams of each other.

    Parameters
    ----------
    word:
        The input string.  May contain any characters; only the sort order
        matters, so non-letter characters are preserved as-is.

    Returns
    -------
    str
        Sorted uppercase representation of *word*.

    Examples
    --------
    >>> signature_of("listen")
    'EILNST'
    >>> signature_of("silent")
    'EILNST'
    >>> signature_of("Triangle")
    'AAEGILNRT'
    """
    return "".join(sorted(word.upper()))
