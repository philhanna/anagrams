# anagrams

```
usage: anagrams [OPTION]... [WORD]
Finds anagrams of all subsets of the specified word of sufficient length.

options:
  -h, --help               display this help text and exit
  -n, --length=NUM         limits output to words of length >= NUM (default=3)
  -f, --full               include only words the same length as the input
```

## Source

The problem is stated on page 150 the book
[*The Pragmatic Programmer, 20th Anniversary Edition*](https://www.amazon.com/Pragmatic-Programmer-journey-mastery-Anniversary/dp/0135957052)
by David Thomas and Andrew Hunt.

## Installation

```
go install github.com/philhanna/anagrams/anagrams@latest
```

## References
- [Github repository](https://github.com/philhanna/anagrams)
- [jsonpp in Go](https://go.dev/play/p/1raEIAEr_Vt)
