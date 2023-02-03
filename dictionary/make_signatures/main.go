package main

import (
	"anagrams"
	"bufio"
	"encoding/json"
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
		Signature string   `json:"signature"`
		Words     []string `json:"words"`
	}

	// Open the input file
	if fp, err = os.Open("../words.txt"); err != nil {
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

	// Open the output file
	if out, err = os.Create("words.json"); err != nil {
		log.Fatal(err)
	}
	defer out.Close()
	nBytes, err := out.Write(jsonbytes)
	log.Printf("nBytes=%d, err=%v\n", nBytes, err)
}
