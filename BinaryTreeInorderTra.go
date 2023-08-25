
 package main
 // Definition for a binary tree node.
type TreeNode struct {
      Val int
      Left *TreeNode
      Right *TreeNode
  }
 
 func inorderTraversal(root *TreeNode) (res []int) {
	if root == nil {
		return 
	}
	
	var traversal func(node *TreeNode) 
	traversal = func(node *TreeNode) {
		if node == nil {
			return
		}
		traversal(node.Left)
		res = append(res, node.Val)
		traversal(node.Right)
	}
	traversal(root)
	return res
}