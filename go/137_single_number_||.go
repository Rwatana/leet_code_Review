package leetcodereview

// singleNumber finds the element that appears only once in an array where every other element appears exactly three times.
func singleNumber(nums []int) int {
  // seenOnce holds bits which have appeared exactly once so far
  // seenTwice holds bits which have appeared exactly twice so far
  seenOnce, seenTwice := 0, 0

   // Iterate through each number in the array
  for _, num := range nums {
    // Update seenOnce:
    // 1. XOR the current value of seenOnce with num.
    // 2. Then remove bits that are present in seenTwice using the AND NOT operator (&^).

    seenOnce = (seenOnce ^ num) &^ seenTwice
    // Update seenTwice:
    // 1. XOR the current value of seenTwice with num.
    // 2. Then remove bits that are now present in the updated seenOnce.

    seenTwice = (seenTwice ^ num) &^ seenOnce
  }

   // At the end, seenOnce contains the number that appears only once
  return seenOnce
}