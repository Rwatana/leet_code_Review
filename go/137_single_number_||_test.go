package leetcodereview

import (
	"testing"
)

// singleNumber finds the element that appears only once in an array where every other element appears exactly three times.
func TestSingleNumber(t *testing.T) {
	tests := []struct {
		name     string
		input    []int
		expected int
	}{
		{
			name:     "Basic input",
			input:    []int{2, 2, 3, 2},
			expected: 3,
		},
		{
			name:     "Negative number input",
			input:    []int{-2, -2, -3, -2},
			expected: -3,
		},
		{
			name:     "Single input",
			input:    []int{1},
			expected: 1,
		},
	}

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			result := singleNumber(tc.input)
			if result != tc.expected {
				t.Errorf("Expected %d but got %d", tc.expected, result)
			}
		})
	}
}
