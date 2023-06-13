package main

// This is a tool that will create a copy of words.txt with signatures
// attached and write it to stdout.
//
// A word's signature in this case is just the sorted set of all its
// characters appended together into a new string.  This signature will
// be used as a key in a map of signatures to lists of words in the
// dictionary that has that same signature.  For example:
//  sigmap["CDDEEI"] == ["DECIDE", "DEICED"]
//
// The map will be serialized as JSON and written to stdout.

import (
	"bufio"
	"encoding/json"
	"log"
	"os"

	"github.com/philhanna/anagrams"
)

const (
	WORDS = "words.txt"
)

func main() {

	var fp *os.File
	var err error

	// Open the input file
	if fp, err = os.Open(WORDS); err != nil {
		log.Fatal(err)
	}
	defer fp.Close()

	// Create a map in which to save signatures mapped to the words
	// that have them
	sigmap := make(map[string][]string)

	// Read it line by line
	scanner := bufio.NewScanner(fp)
	for scanner.Scan() {
		word := scanner.Text()
		sig := anagrams.SignatureOf(word)
		list, ok := sigmap[sig]
		if !ok {
			// list = make([]string, 0)
			sigmap[sig] = list
		}
		sigmap[sig] = append(sigmap[sig], word)
	}

	jsonbytes, err := json.Marshal(sigmap)

	nBytes, err := os.Stdout.Write(jsonbytes)
	log.Printf("nBytes=%d, err=%v\n", nBytes, err)
}
