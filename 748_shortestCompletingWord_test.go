package main

import (
	"strings"
	"testing"
)

// Function to count character occurrences in a string
func countAlphabets(s string) [26]int {
	var count [26]int
	for _, ch := range s {
		if ch >= 'a' && ch <= 'z' {
			count[ch-'a']++
		}
	}
	return count
}

// Function to check if a word include all required letters
func isCompletingWord(word string, required [26]int) bool {
	wordCount := countCharacters(word)
	for i := 0; i < 26; i++ {
		if wordCount[i] < required[i] {
			return false
		}
	}
	return true
}

// Function to find the shortest completing word
func shortestCompletingWord(licensePlate string, words []string) string {
	var licenseString string
	for _, ch := range licensePlate {
		lowerCh := strings.ToLower(string(ch))
		if lowerCh >= "a" && lowerCh <= "z" {
			licenseString += strings.ToLower(string(ch))
		}
	}
	required := countAlphabets(licenseString)

	shortestWord := ""
	for _, word := range words {
		if isCompletingWord(word, required) {
			if shortestWord == "" || len(word) < len(shortestWord) {
				shortestWord = word
			}
		}
	}
	return shortestWord
}

func TestCountCharacters(t *testing.T) {
	tests := []struct {
		name         string
		licensePlate string
		words        []string
		expected     string
	}{
		{"Upper char case", "s PSt", []string{"step", "steps", "stripe", "stepple"}, "steps"},
		{"Include number case", "1s3 456", []string{"looks", "pest", "stew", "show"}, "pest"},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()
			result := shortestCompletingWord(tt.licensePlate, tt.words)
			if result != tt.expected {
				t.Errorf("got %v, want %v", result, tt.expected)
			}
		})
	}
}
