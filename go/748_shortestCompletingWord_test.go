package leetcodereview

import (
	"testing"
)

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
