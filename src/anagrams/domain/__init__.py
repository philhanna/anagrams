# anagrams.domain
"""Domain layer: pure business logic with no I/O or framework dependencies.

Modules
-------
signature
    Computes a canonical *signature* for a word (sorted uppercase letters)
    so that anagrams share the same key.
subsets
    Enumerates every non-empty subset of a string, optionally filtered by
    minimum length.
permutations
    Generates every permutation of a string's characters.
"""
