package leetcodereview

import (
	"testing"
)

func TestReorganizeString(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected string
		hasError bool
	}{
		{
			name:     "Early return test: non lowercase",
			input:    "aA",
			expected: "",
			hasError: true,
		},
		{
			name:     "Early return test: high frequency",
			input:    "aaaabc",
			expected: "",
			hasError: true,
		},
		{
			name:     "Three characters",
			input:    "aab",
			expected: "aba",
			hasError: false,
		},
		{
			name:     "Three same characters",
			input:    "aaa",
			expected: "",
			hasError: true,
		},
	}

	for _, tc := range tests {
		tc := tc // capture range variable
		t.Run(tc.name, func(t *testing.T) {
			result, err := reorganizeString(tc.input)
			if tc.hasError {
				if err == nil {
					t.Errorf("Expected error for input %q, but got result: %q", tc.input, result)
				}
			} else {
				if err != nil {
					t.Errorf("Expected valid result for input %q, but got error: %v", tc.input, err)
				} else if result != tc.expected {
					t.Errorf("Expected %q for input %q, but got %q", tc.expected, tc.input, result)
				}
			}
		})
	}
}
