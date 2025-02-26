package leetcodereview

import (
	"testing"
)

// TestBuddyStrings checks the function against different inputs using t.Run.
// It tests if two strings can be made equal by swapping exactly two letters in the first string.
func TestBuddyStrings(t *testing.T) {
    tests := []struct {
        name     string
        s        string
        goal     string
        expected bool
    }{
        {
            name:     "two strings are buddy strings",
            s:        "ab",
            goal:     "ba",
            expected: true,
        },
        {
            name:     "two strings are not buddy strings",
            s:        "ef",
            goal:     "cd",
            expected: false,
        },
        {
            name:     "the given s is equal to goal and return false",
            s:        "ab",
            goal:     "ab",
            expected: false,
        },
        {
            name:     "the given s is equal to goal and return true",
            s:        "aa",
            goal:     "aa",
            expected: true,
        },
    }

    for _, test := range tests {
        t.Run(test.name, func(t *testing.T) {
            result := buddyStrings(test.s, test.goal)
            if result != test.expected {
                t.Errorf("For test %s: expected %v, but got %v", test.name, test.expected, result)
            }
        })
    }
}
