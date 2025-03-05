package leetcodereview

// countArrangement returns the number of beautiful arrangements that can be made with the numbers 1 to n.
// A beautiful arrangement is one where for every position i (1 <= i <= n), either i is divisible by the number at position i or the number at position i is divisible by i.
func countArrangement(numElements int) int {
	isNumberUsed := make([]bool, numElements+1)
	return backtrack(numElements, 1, isNumberUsed)
}

// backtrack is a helper function that recursively calculates the number of beautiful arrangements that can be made.
// It takes the current position, the total number of elements, and a slice of used numbers as input.
// It returns the number of valid permutations that can be made.
func backtrack(numElements, index int, isNumberUsed []bool) int {
	if index > numElements {
		return 1
	}

	// Try all possible numbers at the current index
	validArrangements := 0
	for candidateNumber := 1; candidateNumber <= numElements; candidateNumber++ {
		if !isNumberUsed[candidateNumber] && isValidPlacement(index, candidateNumber) {
			isNumberUsed[candidateNumber] = true
			validArrangements += backtrack(numElements, index+1, isNumberUsed)
			isNumberUsed[candidateNumber] = false
		}
	}
	return validArrangements
}

// isValidPlacement checks whether a number can be placed at the given index
func isValidPlacement(index int, candidateNumber int) bool {
	return candidateNumber%index == 0 || index%candidateNumber == 0
}
