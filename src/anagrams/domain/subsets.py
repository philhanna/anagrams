"""Subset enumeration over a string's characters.

Used by the search service to generate every possible sub-word of the user's
input so that the dictionary can be queried for each one.
"""


def all_subsets(s: str, length: int) -> list[str]:
    """Return every non-empty subset of *s* whose length is at least *length*.

    Subsets are generated via bitmask enumeration: for an *n*-character string
    there are ``2**n - 1`` non-empty subsets.  Bit *i* of the mask being set
    means character ``s[i]`` is included in that subset.

    Parameters
    ----------
    s:
        Source string whose characters will be combined into subsets.
        Duplicate characters are treated independently (each occurrence gets
        its own position).
    length:
        Minimum number of characters a subset must contain to be included in
        the result.  Pass ``1`` to receive all non-empty subsets.

    Returns
    -------
    list[str]
        All subsets of *s* with ``len(subset) >= length``, in bitmask order
        (not lexicographically sorted).

    Examples
    --------
    >>> all_subsets("abc", 2)
    ['ab', 'ac', 'bc', 'abc']
    """
    n = len(s)
    result = []
    for mask in range(1, 1 << n):
        subset = "".join(s[i] for i in range(n) if mask & (1 << i))
        if len(subset) >= length:
            result.append(subset)
    return result
