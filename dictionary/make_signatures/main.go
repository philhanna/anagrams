package main

import (
	"anagrams"
	"bufio"
	"fmt"
	"log"
	"os"
)

/*
This tool will create a copy of words.txt with signatures attached
*/
func main() {

	var fp, out *os.File
	var err error

	type HashedWord struct {
		Words []string `json:"words"`
	}

	// Open the input file
	if fp, err = os.Open("../somewords.txt"); err != nil {
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
		sig := anagrams.GetSignature(word)
		sigmap[sig] = append(sigmap[sig], word)
	}

	// Open the output file
	if out, err = os.Create("words-sig.json"); err != nil {
		log.Fatal(err)
	}
	defer out.Close()

}
