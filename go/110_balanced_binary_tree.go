package leetcodereview

// Main function to check if a tree is balanced.
// If the tree is balanced, return true.
// If the tree is unbalanced, return false.
func isBalanced(root *TreeNode) bool {
	return getHeightOrMinusOneIfUnbalanced(root) != -1
}

// getHeightOrMinusOneIfUnbalanced returns the height of the tree if it is balanced.
// If the tree is unbalanced, it returns -1.
func getHeightOrMinusOneIfUnbalanced(root *TreeNode) int {
	if root == nil {
		return 0
	}

	leftHeight := getHeightOrMinusOneIfUnbalanced(root.Left)
	if leftHeight == -1 {
		return -1
	}

	rightHeight := getHeightOrMinusOneIfUnbalanced(root.Right)
	if rightHeight == -1 {
		return -1
	}

	if abs(leftHeight-rightHeight) > 1 {
		return -1
	}

	return max(leftHeight, rightHeight) + 1
}

// Utility function to get the absolute difference.
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

// Utility function to get the maximum of two numbers.
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
