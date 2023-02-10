package main

import (
	"encoding/json"
	"fmt"
	"io"
	"os"
	"sort"

	"github.com/philhanna/anagrams"
)

// Takes a string from the command line and finds all words whose
// letters are contained in the string. Only words of length
// greater than or equal to 3 are included. Output is written
// to stdout.
func main() {

	// Get the word from the command line
	if len(os.Args) == 1 {
		fmt.Fprintln(os.Stderr, "No word specified")
		os.Exit(1)
	}
	word := os.Args[1]

	// Start loading the dictionary
	loaded := make(chan error)
	sigmap := make(map[string][]string)
	go loadDictionary(loaded, &sigmap)

	// Wait for dictionary load to complete
	err := <-loaded
	if err != nil {
		fmt.Fprintf(os.Stderr, "Could not load signature map: %v\n", err)
		os.Exit(1)
	}

	// Examine all subsets of the word with length >= 3 and store them in a map
	outset := make(map[string]int)
	subsets := anagrams.AllSubsets(word)
	for _, subset := range subsets {

		// Compute the subset's signature
		signature := anagrams.SignatureOf(subset)

		// Look up all words with the same signature
		list, ok := sigmap[signature]
		if ok {
			for _, newWord := range list {
				outset[newWord] += 1
			}
		}
	}

	// Sort the output set and write it to stdout
	keys := make([]string, 0, len(outset))
	for key := range outset {
		keys = append(keys, key)
	}
	sort.Strings(keys)
	for _, key := range keys {
		fmt.Printf("%s\n", key)
	}
}

// Loads the signature map
func loadDictionary(loaded chan error, pSigmap *map[string][]string) {
	fp, err := os.Open("../sigmap.json")
	if err != nil {
		loaded <- err
		return
	}
	jsonBytes, err := io.ReadAll(fp)
	if err != nil {
		loaded <- err
		return
	}
	err = json.Unmarshal(jsonBytes, pSigmap)
	loaded <- err
}
