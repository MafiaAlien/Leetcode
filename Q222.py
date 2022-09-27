# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self._postOrder(root)

    def _postOrder(self, node):
        if not node:
            return 0
        
        left = node.left 
        right = node.right 
        leftDepth, rightDepth = 0 ,0 

        while left:
            left = left.left 
            leftDepth += 1
        while right:
            right = right.right 
            rightDepth += 1 
        
        if leftDepth == rightDepth:
            res = (2 << leftDepth) - 1 #满二叉树节点计算公式（位运算）
            return res 
        
        leftNum = self._postOrder(node.left)
        rightNum = self._postOrder(node.right)
        return leftNum + rightNum + 1