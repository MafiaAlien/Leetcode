# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Recursive
from matplotlib import collections


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        res = [] # 保存结果的数组
        rest = targetSum - root.val # 根节点的叶子结点值
        path = [root.val] # 当前路径点
        self._getPath(root, rest, res, path)
        return res 
    
    def _getPath(self, node, rest, res, path):
        # 如果是叶子结点，并且剩余值刚好为0，那么就是需要的路径点
        if not node.left and not node.right and rest == 0:
            res.append(path[:])

        if node.left:
            path.append(node.left.val) # 深度搜索
            self._getPath(node.left, rest - node.left.val, res, path)
            path.pop() # 回溯

        if node.right:
            path.append(node.right.val)
            self._getPath(node.right, rest - node.right.val, res, path)
            path.pop()
        