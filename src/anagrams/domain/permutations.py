"""Permutation generation for a string's characters.

Provided as a pure-Python, dependency-free alternative to
``itertools.permutations`` for use within the domain layer.
"""


def permutations(s: str) -> list[str]:
    """Return all permutations of the characters in *s*.

    Uses a recursive, pick-and-recurse algorithm: for each position *i*,
    choose ``s[i]`` as the first character and prepend it to every
    permutation of the remaining characters.

    The result contains ``len(s)!`` strings.  Duplicate characters in *s*
    will produce duplicate permutations in the output.

    Parameters
    ----------
    s:
        The string whose characters will be permuted.  An empty string or a
        single-character string is returned as a one-element list.

    Returns
    -------
    list[str]
        All ``len(s)!`` permutations of *s*, in the order produced by the
        recursive traversal.

    Examples
    --------
    >>> permutations("ab")
    ['ab', 'ba']
    >>> permutations("abc")
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    >>> permutations("")
    ['']
    """
    if len(s) <= 1:
        return [s]
    result = []
    for i, char in enumerate(s):
        rest = s[:i] + s[i + 1 :]
        for perm in permutations(rest):
            result.append(char + perm)
    return result
