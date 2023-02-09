package anagrams

// Recursive algorithm to find all Permutations of a string.
func Permutations(s string) []string {
	var newPerms []string
	var first, rest string

	if len(s) == 1 {
		newPerms = append(newPerms, s)
	} else {
		for i, ch := range s {
			first = string(ch)
			rest = s[0:i] + s[i+1:]
			for _, perm := range Permutations(rest) {
				newPerms = append(newPerms, first+perm)
			}
		}
	}
	return newPerms
}