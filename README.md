# anagrams

## Source

The problem is stated on page 150 the book *The Pragmatic Programmer, 20th Anniversary Edition* by David Thomas and Andrew Hunt.

## Algorithms

To generate all permutations of a string:
```
// Recursive algorithm to find all permutations of a string.
func permutations(s string) []string {
	var newPerms []string
	var first, rest string

	if len(s) == 1 {
		newPerms = append(newPerms, s)
	} else {
		for i, ch := range s {
			first = string(ch)
			rest = s[0:i] + s[i+1:]
			for _, perm := range permutations(rest) {
				newPerms = append(newPerms, first+perm)
			}
		}
	}
	return newPerms
}
```
## References
- [jsonpp in Go](https://go.dev/play/p/1raEIAEr_Vt)
