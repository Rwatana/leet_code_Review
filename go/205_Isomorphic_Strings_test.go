package leetcodereview

import "testing"

// TestIsIsomorphic tests the isIsomorphic function with various test cases.
func TestIsIsomorphic(t *testing.T) {
	tests := []struct {
		name           string
		source              string
		target              string
		expectedResult bool
	}{
		{
			name:           "Identical strings",
			source:              "abc",
			target:              "efg",
			expectedResult: true,
		},
		{
			name:           "Same size strings",
			source:              "egg",
			target:              "add",
			expectedResult: true,
		},
		{
			name:           "Different size strings",
			source:              "foo",
			target:              "hogehoge",
			expectedResult: false,
		},
		{
			name:           "same source character for different target characters",
			source:              "bar",
			target:              "foo",
			expectedResult: false,
		},
		{
			name:           "same target character for different source characters",
			source:              "foo",
			target:              "bar",
			expectedResult: false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := isIsomorphic(tt.source, tt.target)
			if result != tt.expectedResult {
				t.Errorf("isIsomorphic(%q, %q) = %v; expected %v", tt.source, tt.target, result, tt.expectedResult)
			}
		})
	}
}
