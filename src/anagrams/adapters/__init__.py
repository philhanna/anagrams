# anagrams.adapters
"""Adapters layer: concrete implementations of the port interfaces.

Each adapter fulfils one port contract and handles a specific I/O mechanism.
Adapters are the only layer allowed to perform file I/O, network calls, or
other infrastructure-level operations.

Modules
-------
json_dictionary
    ``JsonDictionaryAdapter`` — loads the prebuilt signature map from a JSON
    file (either the bundled ``anagrams.data/sigmap.json`` or a caller-supplied
    path) and satisfies the ``DictionaryPort`` contract.
"""
