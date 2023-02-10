// anagrams takes a string from the command line and finds all words
// whose letters are contained in the string. Only words of length
// greater than or equal to an optional limit are included. The matching
// words are written to stdout.
package main

import (
	"flag"
	"fmt"
	"os"

	"github.com/philhanna/anagrams"
)

func main() {

	// Handle the command line
	word, length, full := parseArgs()
	if word == "" {
		fmt.Fprintln(os.Stderr, "anagrams: No word specified")
		os.Exit(1)
	}
	if full {
		length = len(word)
	}

	// Get the anagrams
	if keys, err := anagrams.Search(word, length); err != nil {
		fmt.Fprintln(os.Stderr, err)
	} else {
		for _, key := range keys {
			fmt.Printf("%s\n", key)
		}

	}
}

// Defines and parses the command line arguments
func parseArgs() (string, int, bool) {
	const usage = `usage: anagrams [OPTION]... [WORD]
Finds anagrams of all subsets of the specified word of sufficient length.

options:
  -h, --help               display this help text and exit
  -n, --length=NUM         limits output to words of length >= NUM (default=3)
  -f, --full               include only words the same length as the input

Source: <https://github.com/philhanna/anagrams>
`
	// Override the flag package's Usage function so that our own usage
	// message will be displayed.
	flag.Usage = func() {
		fmt.Fprint(os.Stderr, usage)
	}
	const defaultLength = 3
	var length int = defaultLength
	var full bool = false
	word := ""
	flag.IntVar(&length, "n", 3, "limits output to only those words of length >= NUM (short)")
	flag.IntVar(&length, "length", 3, "limits output to only those words of length >= NUM")
	flag.BoolVar(&full, "f", false, "include only words the same length as the input")
	flag.BoolVar(&full, "full", false, "include only words the same length as the input")
	flag.Parse()
	if flag.NArg() > 0 {
		word = flag.Arg(0)
	}
	return word, length, full
}
