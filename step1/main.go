package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for {
		scanner.Scan()
		text := scanner.Text()
		if len(text) == 0 {
			break
		} else {
		for _, perm := range permutations(text) {
			fmt.Println(perm)
		}
	}
	}
}

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