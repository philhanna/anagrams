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

	// Open the input file
	if fp, err = os.Open("../words.txt"); err != nil {
		log.Fatal(err)
	}
	defer fp.Close()

	// Open the output file
	if out, err = os.Create("words-sig.txt"); err != nil {
		log.Fatal(err)
	}
	defer out.Close()

	// Read it line by line
	scanner := bufio.NewScanner(fp)
	for scanner.Scan() {
		word := scanner.Text()
		sig := anagrams.GetSignature(word)
		fmt.Fprintf(out, "%s %s\n", sig, word)
	}
}
