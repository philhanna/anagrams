package anagrams

import (
	"sort"
	"strings"
)

// SignatureOf returns the signature of a word
func SignatureOf(word string) string {
	s := strings.Split(strings.ToUpper(word), "")
	sort.Strings(s)
	sig := strings.Join(s, "")
	return sig
}
