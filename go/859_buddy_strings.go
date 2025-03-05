package leetcodereview

const (
	diffCount = 2 // Number of differences required to check for a valid swap
)

// buddyStrings checks if two strings s and goal can be made equal by swapping exactly two letters in s.
// - If the strings have different lengths, return false.
// - If the strings are identical, it checks if there are any duplicate characters in s.
// - If the strings are not identical, it finds the positions where they differ and checks if swapping those two positions makes the strings equal.
func buddyStrings(s string, goal string) bool {
	if len(s) != len(goal) {
		return false
	}

	// If s and goal are identical, check if there are any duplicate characters in s
	if s == goal {
		return hasDuplicateCharacter(s)
	}

	// Find the positions where s and goal differ
	differentIndices := findMismatchIndices(s, goal)

	// If there are exactly two differences, check if swapping those two indices makes the strings equal
	return canSwapToMatch(s, goal, differentIndices)
}

// hasDuplicateCharacter checks if there are any duplicate characters in string s.
// It returns true if there are duplicates, otherwise false.
// This is used when s and goal are the same, to check if swapping identical characters results in no change.
func hasDuplicateCharacter(s string) bool {
	seen := make(map[rune]struct{})
	for _, char := range s {
		if _, exists := seen[char]; exists {
			return true
		}
		seen[char] = struct{}{}
	}
	return false
}

// findMismatchIndices finds the positions where s and goal differ.
// It returns a slice containing the indices where the characters of s and goal do not match.
func findMismatchIndices(s, goal string) []int {
	var differentIndices []int
	for i := 0; i < len(s); i++ {
		if s[i] != goal[i] {
			differentIndices = append(differentIndices, i)
		}
	}
	return differentIndices
}

// canSwapToMatch checks if swapping the two characters at the indices in differentIndices makes s equal to goal.
// It returns true if swapping the characters at these two positions makes the strings equal, otherwise false.
func canSwapToMatch(s, goal string, differentIndices []int) bool {
	if len(differentIndices) != diffCount {
		return false
	}

	i, j := differentIndices[0], differentIndices[1]
	return s[i] == goal[j] && s[j] == goal[i]
}
