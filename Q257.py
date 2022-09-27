# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        res, path = [], []
        self._getPath(root, path, res)
        return res

    def _getPath(self, node, path:List, res:List):
        # 路径点添加节点值
        path.append(str(node.val)) 
        # 终止条件
        if not node.left and not node.right:
            res.append('->'.join(path)) 

        if node.left:
            self._getPath(node.left, path, res) 
            path.pop() # 这里的pop是回溯操作，弹出之前递归存储的路径点value

        if node.right:
            self._getPath(node.right, path, res) 
            path.pop()   