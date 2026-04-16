# anagrams.ports
"""Ports layer: abstract interfaces that decouple the application from infrastructure.

Each port is an abstract base class (ABC) that the application layer depends on.
Concrete implementations live in the ``adapters`` package and are injected at
runtime, keeping the application layer testable in isolation.

Modules
-------
dictionary_port
    ``DictionaryPort`` — secondary port for looking up words by signature.
"""
