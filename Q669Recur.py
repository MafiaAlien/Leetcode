# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # if root.val < low return right node 
        # if root.val > high return left node 

        if not root:
            # 终止条件
            return None  

        if root.val < low:
            # 如果小于边界最小值，则继续向右递归，因为左子树会比当前节点值更小所以舍弃
            # 该方法已经包括了返回的节点及其满足边界条件的所有子节点
            # 返回满足边界条件的右子树回溯让上一层的父节点接住，断开原不满足边界的原节点及其父节点的指向达到
            # 删除节点的目的
            right = self.trimBST(root.right, low, high)
            return right 

        if root.val > high:
            # 同上
            left = self.trimBST(root.left, low, high)
            return left 

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root 