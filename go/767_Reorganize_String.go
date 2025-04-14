package leetcodereview

import (
	"errors"
	"regexp"
)

// CharItem stores a character and its frequency count.
type CharItem struct {
	char  byte
	count int
}

// CharMaxHeap is a max-heap that stores CharItems.
type CharMaxHeap struct {
	items []*CharItem
}

// NewCharMaxHeap creates a new instance of CharMaxHeap.
func NewCharMaxHeap() *CharMaxHeap {
	return &CharMaxHeap{items: []*CharItem{}}
}

// Push adds a new element to the heap and maintains the heap property.
func (h *CharMaxHeap) Push(item *CharItem) {
	h.items = append(h.items, item)
	h.heapifyUp(len(h.items) - 1)
}

// Pop removes and returns the top element (the one with the highest count) from the heap.
func (h *CharMaxHeap) Pop() *CharItem {
	if len(h.items) == 0 {
		return nil
	}
	top := h.items[0]
	lastIndex := len(h.items) - 1
	h.items[0] = h.items[lastIndex]
	h.items = h.items[:lastIndex]
	h.heapifyDown(0)
	return top
}

// Len returns the number of elements in the heap.
func (h *CharMaxHeap) Len() int {
	return len(h.items)
}

// heapifyUp moves the element at the given index up to maintain the heap property.
func (h *CharMaxHeap) heapifyUp(index int) {
	for index > 0 {
		parent := (index - 1) / 2
		if h.items[index].count > h.items[parent].count {
			h.items[index], h.items[parent] = h.items[parent], h.items[index]
			index = parent
		} else {
			break
		}
	}
}

// heapifyDown moves the element at the given index down to maintain the heap property.
func (h *CharMaxHeap) heapifyDown(index int) {
	length := len(h.items)
	for {
		left := 2*index + 1
		right := 2*index + 2
		largest := index

		if left < length && h.items[left].count > h.items[largest].count {
			largest = left
		}
		if right < length && h.items[right].count > h.items[largest].count {
			largest = right
		}
		if largest != index {
			h.items[index], h.items[largest] = h.items[largest], h.items[index]
			index = largest
		} else {
			break
		}
	}
}

var hasNonLowerAlphabet = regexp.MustCompile(`[^a-z]`)

// reorganizeString rearranges the characters in the string s so that no two adjacent characters are the same.
// It returns the rearranged string and an error if rearrangement is not possible.
func reorganizeString(s string) (string, error) {
	// Check if the input string contains any non-lowercase English letters.
	if hasNonLowerAlphabet.MatchString(s) {
		return "", errors.New("only lowercase English letters are allowed")
	}

	n := len(s)
	freq := make(map[byte]int)
	for i := 0; i < n; i++ {
		freq[s[i]]++
	}

	// Calculate the maximum allowed frequency for any character.
	maxAllowed := (n + 1) / 2

	// Early return if rearrangement is impossible.
	for _, count := range freq {
		if count > maxAllowed {
			return "", errors.New("rearrangement not possible")
		}
	}

	heap := NewCharMaxHeap()
	for char, count := range freq {
		heap.Push(&CharItem{char: char, count: count})
	}

	result := make([]byte, 0, n)
	var prev *CharItem = nil

	// Process one item at a time.
	for heap.Len() > 0 {
		current := heap.Pop()
		result = append(result, current.char)
		current.count--

		// If there is a previous element, push it back into the heap.
		if prev != nil {
			heap.Push(prev)
			prev = nil
		}

		// If the current element still has a remaining count, store it as the previous element.
		if current.count > 0 {
			prev = current
		}
	}

	return string(result), nil
}
