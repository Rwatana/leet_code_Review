package leetcodereview

import "testing"

// TestCountArrangement tests the countArrangement function with various test cases.
func TestCountArrangement(t *testing.T) {
	// Define test cases
	tests := []struct {
		name     string
		n        int
		expected int
	}{
		{
			name:     "base test",
			n:        1,
			expected: 1,
		},
		{
			name:     "large number test",
			n:        15,
			expected: 24679,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := countArrangement(tt.n)
			if result != tt.expected {
				t.Errorf("countArrangement(%d) = %d, want %d", tt.n, result, tt.expected)
			}
		})
	}
}
