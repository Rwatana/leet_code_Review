package leetcodereview

import (
	"testing"
)

// TestMostCommonWord checks the function against different inputs using t.Run.
func TestMostCommonWord(t *testing.T) {
	tests := []struct {
		name      string
		paragraph string
		banned    []string
		expected  string
	}{
		{"Basic case", "Bob hit a ball, the hit BALL flew far after it was hit.", []string{"hit"}, "ball"},
		{"Upper and Lower case words", "Hello, hello world! Hello world.", []string{"hello"}, "world"},
		{"Multiple occurrences", "a a a b b c c c c", []string{"c"}, "a"},
		{"Single word", "a.", []string{}, "a"},
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			result := mostCommonWord(test.paragraph, test.banned)
			if result != test.expected {
				t.Errorf("mostCommonWord(%q, %v) = %q; expected %q",
					test.paragraph, test.banned, result, test.expected)
			}
		})
	}
}
