/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// find tilt of a binary tree
// tilt of a node is the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values
func findTilt(root *TreeNode) int {
	treeTilt := 0
	getSum(root, &treeTilt)
	return treeTilt
}

// get sum of all nodes in the tree and update tilt
func getSum(node *TreeNode, tilt *int) int {
	if node == nil {
		return 0
	}

	leftSum, rightSum := getSum(node.Left, tilt), getSum(node.Right, tilt)
	treeDiff := leftSum - rightSum
	if treeDiff < 0 {
		treeDiff = -treeDiff
	}
	*tilt += treeDiff

	return leftSum + rightSum + node.Val
}