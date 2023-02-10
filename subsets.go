package anagrams

// Given a string, returns all subsets of that string
func AllSubsets(s string, length int) []string {
	var subsets []string
	limit := 1 << len(s)
	for bits := 0; bits < limit; bits++ {
		newWord := ""
		for i := 0; i < len(s); i++ {
			mask := 1 << i
			and := bits & mask
			if and != 0 {
				chr := s[i]
				newWord += string(chr)
			}
		}
		if len(newWord) >= length {
			subsets = append(subsets, newWord)
		}
	}
	return subsets
}
