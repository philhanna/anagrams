# Changelog

This project adheres to [Semantic Versioning],
and the format is based on [Keep a Changelog].

## [Unreleased]

### Changed
- Ported project from Go to Python using a hexagonal (ports-and-adapters)
  architecture: domain layer (signature, subsets, permutations), ports
  (`DictionaryPort`), adapters (`JsonDictionaryAdapter`), and application
  (`SearchService`).
- Replaced Go CLI with a Python `argparse`-based CLI (`anagrams.cli`).
- Replaced Go test suite with pytest.
- Added `build-sigmap` entry point (`anagrams.build_sigmap`) for regenerating
  the bundled `sigmap.json` from a word list.
- Updated `README.md` and `.gitignore` for Python tooling.

### Removed
- All Go source files, binaries, module files (`go.mod`, `go.sum`), and the
  Go design document.

---

[Semantic Versioning]: https://semver.org/
[Keep a Changelog]: https://keepachangelog.com/
