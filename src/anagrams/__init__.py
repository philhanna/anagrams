# anagrams
"""Anagram finder implementing a hexagonal (ports-and-adapters) architecture.

The package is structured into four layers:

- ``domain``    — pure functions for signature computation, subset enumeration,
                  and permutation generation; no I/O, no dependencies.
- ``ports``     — abstract base classes that define the contracts between the
                  application layer and the outside world.
- ``adapters``  — concrete implementations of those contracts (e.g. loading the
                  word list from a bundled JSON file).
- ``application`` — the ``SearchService`` that orchestrates domain logic and
                    port calls to answer a user query.

The ``cli`` module and ``build_sigmap`` module are the primary entry points.
"""
