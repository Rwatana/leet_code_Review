package main

import (
	"strings"
	"testing"
)

// Function to count character occurrences in a string
func countCharacters(s string) [26]int {
	var count [26]int
	for _, ch := range s {
		if ch >= 'a' && ch <= 'z' {
			count[ch-'a']++
		}
	}
	return count
}

// Function to check if a word include all required letters
func isIncludingWord(word string, required [26]int) bool {
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
		if (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') {
			licenseString += strings.ToLower(string(ch))
		}
	}
	required := countCharacters(licenseString)

	shortestWord := ""
	for _, word := range words {
		if isIncludingWord(word, required) {
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
		{"test1", "1s3 PSt", []string{"step","steps","stripe","stepple"}, "steps"},
		{"test2", "1s3 456", []string{"looks","pest","stew","show"}, "pest"},
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


