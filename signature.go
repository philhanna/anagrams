package anagrams

import (
	"sort"
	"strings"
)

// GetSignature returns the signature of a word
func GetSignature(word string) string {
	s := strings.Split(word, "")
	sort.Strings(s)
	sig := strings.Join(s, "")
	return sig
}
