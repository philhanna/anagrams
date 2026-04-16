# anagrams.application
"""Application layer: use-case services that orchestrate domain logic and ports.

Services in this layer coordinate calls to the domain layer and depend on port
interfaces (not concrete adapters), keeping business logic infrastructure-free.

Modules
-------
search_service
    ``SearchService`` — finds all dictionary words that are anagrams of any
    subset of a given input word.
"""
