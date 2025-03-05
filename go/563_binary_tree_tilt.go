package leetcodereview

import (
	"testing"
)

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// Finds the tilt of a binary tree.
// The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values.
func findTilt(root *TreeNode) int {
	totalTilt := 0
	computeSubtreeSum(root, &totalTilt)
	return totalTilt
}

// Computes the sum of all nodes in the subtree while updating the tilt.
// Returns the sum of all nodes in the subtree.
func computeSubtreeSum(node *TreeNode, tilt *int) int {
	if node == nil {
		return 0
	}

	leftSum := computeSubtreeSum(node.Left, tilt)
	rightSum := computeSubtreeSum(node.Right, tilt)
	*tilt += abs(leftSum - rightSum)

	return leftSum + rightSum + node.Val
}

// // Helper function to get the absolute value.
// func abs(x int) int {
// 	if x < 0 {
// 		return -x
// 	}
// 	return x
// }

// Test function for findTilt
func TestFindTilt(t *testing.T) {
	tests := []struct {
		name string
		root *TreeNode
		want int
	}{
		{
			name: "Example 1",
			root: &TreeNode{1, &TreeNode{2, nil, nil}, &TreeNode{3, nil, nil}},
			want: 1,
		},
		{
			name: "Example 2",
			root: &TreeNode{
				4,
				&TreeNode{2, &TreeNode{3, nil, nil}, &TreeNode{5, nil, nil}},
				&TreeNode{9, nil, &TreeNode{7, nil, nil}},
			},
			want: 15,
		},
		{
			name: "Empty Tree",
			root: nil,
			want: 0,
		},
		{
			name: "Single Node",
			root: &TreeNode{1, nil, nil},
			want: 0,
		},
		{
			name: "Unbalanced Tree",
			root: &TreeNode{1, &TreeNode{2, &TreeNode{3, nil, nil}, nil}, nil},
			want: 4,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := findTilt(tt.root)
			if got != tt.want {
				t.Errorf("findTilt() = %d, want %d", got, tt.want)
			}
		})
	}
}
