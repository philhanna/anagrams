// anagrams takes a string from the command line and finds all words
// whose letters are contained in the string. Only words of length
// greater than or equal to an optional limit are included. The matching
// words are written to stdout.
package main

import (
	"embed"
	"encoding/json"
	"flag"
	"fmt"
	"os"
	"sort"

	"github.com/philhanna/anagrams"
)

// The sigmap.json file needs to be part of the executable generated by
// go build or go install
//
//go:embed sigmap.json
var resources embed.FS

func main() {

	// Start loading the dictionary
	loaded := make(chan error)
	sigmap := make(map[string][]string)
	go loadDictionary(loaded, &sigmap)

	// Meanwhile, handle the command line
	word, length := parseArgs()
	if word == "" {
		fmt.Fprintln(os.Stderr, "anagrams: No word specified")
		os.Exit(1)
	}

	// Wait for dictionary load to complete
	err := <-loaded
	if err != nil {
		fmt.Fprintf(os.Stderr, "anagrams: Could not load signature map: %v\n", err)
		os.Exit(1)
	}

	// Examine all subsets of the word of sufficient length (command line option)
	// and store them in a map
	outset := make(map[string]int)
	subsets := anagrams.AllSubsets(word, length)
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
	jsonBytes, err := resources.ReadFile("sigmap.json")
	if err != nil {
		loaded <- err
		return
	}
	err = json.Unmarshal(jsonBytes, pSigmap)
	loaded <- err
}

// Defines and parses the command line arguments
func parseArgs() (string, int){
	const usage = `usage: anagrams [OPTION]... [WORD]
Finds anagrams of all subsets of the specified word of sufficient length.

options:
  -h, --help               display this help text and exit
  -n, --length=NUM         limits output to words of length >= NUM (default=3)

Source: <https://github.com/philhanna/anagrams>
`
	// Override the flag package's Usage function so that our own usage
	// message will be displayed.
	flag.Usage = func() {
		fmt.Fprint(os.Stderr, usage)
	}
	const defaultLength = 3
	var length int = defaultLength
	word := ""
	flag.IntVar(&length, "n", 3, "limits output to only those words of length >= NUM (short)")
	flag.IntVar(&length, "length", 3, "limits output to only those words of length >= NUM")
	flag.Parse()
	if flag.NArg() > 0 {
		word = flag.Arg(0)
	}
	return word, length
}
