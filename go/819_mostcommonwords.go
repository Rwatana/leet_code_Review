package leetcodereview

import (
	"strings"
	"unicode"
)

// sanitizeText processes the input text by converting it to lowercase and extracting words.
func sanitizeText(text string) []string {
	text += " "
	var words []string
	var wordBuffer strings.Builder

	for _, char := range text {
		char = unicode.ToLower(char)
		if unicode.IsLetter(char) {
			wordBuffer.WriteByte(byte(char))
		} else if wordBuffer.Len() > 0 {
			words = append(words, wordBuffer.String())
			wordBuffer.Reset()
		}
	}
	return words
}

// countWordOccurrences counts the number of times each word appears in the list.
func countWordOccurrences(words []string) map[string]int {
	wordsCounts := make(map[string]int)
	for _, word := range words {
		wordsCounts[word]++
	}
	return wordsCounts
}

// removeBannedWords filters out words that are in the banned list.
func removeBannedWords(wordCounts map[string]int, banned []string) {
	for _, word := range banned {
		delete(wordCounts, word)
	}
}

// mostCommonWord finds the most frequently occurring word that is not in the banned list.
func mostCommonWord(paragraph string, banned []string) string {
	words := sanitizeText(paragraph)
	wordsCounts := countWordOccurrences(words)
	removeBannedWords(wordsCounts, banned)

	var mostCommonWord string
	maxCount := 0
	for word, count := range wordsCounts {
		if count > maxCount {
			maxCount = count
			mostCommonWord = word
		}
	}
	return mostCommonWord
}
