package leetcodereview

// singleNumber finds the element that appears only once in an array where every other element appears exactly three times.
func singleNumber(nums []int) int {
	// seenOnce holds bits which have appeared exactly once so far.
	// seenTwice holds bits which have appeared exactly twice so far.
	seenOnce, seenTwice := 0, 0

	// Iterate through each number in the array
	for _, num := range nums {
		// Update seenOnce by XOR-ing it with num and then removing any bits present in seenTwice.
		seenOnce = (seenOnce ^ num) &^ seenTwice

		// Update seenTwice by XOR-ing it with num and then removing any bits present in the updated seenOnce.
		seenTwice = (seenTwice ^ num) &^ seenOnce
	}

	// At the end, seenOnce contains the number that appears only once.
	return seenOnce
}
