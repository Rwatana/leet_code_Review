package leetcodereview

import "testing"

// TestIsBalanced tests the isBalanced function with various test cases.
func TestIsBalanced(t *testing.T) {
	// Create small balanced trees
	smallTree1 := TreeNode{Val: 1, Left: &TreeNode{Val: 2}, Right: &TreeNode{Val: 3}}
	smallTree2 := TreeNode{Val: 4, Left: &TreeNode{Val: 5}, Right: &TreeNode{Val: 6}}

	// Create a balanced tree
	balancedTree := TreeNode{Val: 0, Left: &smallTree1, Right: &smallTree2}

	// Create an unbalanced tree (missing right subtree)
	unbalancedTree := TreeNode{Val: 0, Left: &smallTree1}

	// Define test cases
	tests := []struct {
		name     string
		treeNode *TreeNode
		expected bool
	}{
		{
			name:     "empty tree (nil root)",
			treeNode: nil,
			expected: true,
		},
		{
			name:     "balanced binary tree",
			treeNode: &balancedTree,
			expected: true,
		},
		{
			name:     "unbalanced binary tree",
			treeNode: &unbalancedTree,
			expected: false,
		},
		{
			name:     "single node tree",
			treeNode: &TreeNode{Val: 10},
			expected: true,
		},
		{
			name: "deep unbalanced tree",
			treeNode: &TreeNode{
				Val: 0,
				Left: &TreeNode{
					Val: 1,
					Left: &TreeNode{
						Val: 2,
						Left: &TreeNode{
							Val: 3,
						},
					},
				},
			},
			expected: false,
		},
	}

	// Run test cases
	for _, test := range tests {
		test := test // Avoid range variable issue in goroutines
		t.Run(test.name, func(t *testing.T) {
			res := isBalanced(test.treeNode)
			if res != test.expected {
				t.Errorf("%s: expected %v, but got %v", test.name, test.expected, res)
			}
		})
	}
}
