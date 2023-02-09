package main

import (
	"encoding/json"
	"fmt"
	"io"
	"os"

	"github.com/philhanna/anagrams"
)


func main() {

	// Get the word from the command line
	if len(os.Args) == 1 {
		fmt.Fprintln(os.Stderr, "No word specified")
		os.Exit(1)
	}
	word := os.Args[1]

	// Compute its signature
	signature := anagrams.SignatureOf(word)

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

	// Look up word in dictionary
	list, ok := sigmap[signature]
	if ok {
		for _, aword := range list {
			fmt.Println(aword)
		}
	}
}

func loadDictionary(loaded chan error, pSigmap *map[string][]string) {
	fp, err := os.Open("../words.json")
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
