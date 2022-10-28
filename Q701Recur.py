# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 最重要的是注意回溯过程
        # 终止条件： 如果没有子节点，将添加新节点并返回
        if not root:
            node = TreeNode(val)
            return node  
        
        if root.val > val:
            # 如果当前值小于根节点值，则走左子树，并且用left接住终止条件回溯的节点
            root.left = self.insertIntoBST(root.left, val)
        if root.val < val:
            # 同理如果是大于根节点值则走右子树，并且用right接住回溯回来的新节点
            root.right = self.insertIntoBST(root.right, val)
        return root 