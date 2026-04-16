# anagrams

Finds all valid English words whose letters are a subset of a given input word.

```
usage: anagrams [-h] [-n NUM] [-f] [word]

positional arguments:
  word               input word

options:
  -h, --help         show this help message and exit
  -n NUM, --length NUM
                     limits output to words of length >= NUM (default=3)
  -f, --full         include only words the same length as the input
```

For example, given `triangle`, the tool finds words like `alert`, `grail`,
`liter`, `regal`, and many others.

## Source

The problem is stated on page 150 of
[*The Pragmatic Programmer, 20th Anniversary Edition*](https://www.amazon.com/Pragmatic-Programmer-journey-mastery-Anniversary/dp/0135957052)
by David Thomas and Andrew Hunt.

## Installation

```bash
pip install .
```

Requires Python 3.11 or later.

## Usage

```bash
anagrams triangle
anagrams -n 4 triangle       # only words with 4+ letters
anagrams --full triangle     # only words the same length as the input
```

## Architecture

The package uses a hexagonal (ports-and-adapters) design:

| Layer | Package | Role |
|---|---|---|
| Domain | `anagrams.domain` | Pure functions: signature, subsets, permutations |
| Ports | `anagrams.ports` | Abstract interfaces (e.g. `DictionaryPort`) |
| Adapters | `anagrams.adapters` | Concrete I/O (JSON file lookup) |
| Application | `anagrams.application` | `SearchService` orchestrates domain + ports |

## Building the word list

The bundled `sigmap.json` maps each word signature (sorted uppercase letters)
to the list of matching words.  To rebuild it from a custom word list:

```bash
python -m anagrams.build_sigmap /path/to/words.txt > src/anagrams/data/sigmap.json
```

## Running tests

```bash
pytest
```

## References

- [Github repository](https://github.com/philhanna/anagrams)
