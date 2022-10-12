# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []
        self.inOrder(root, values)

        # 将所有值都加入到一个数组，并且看数组是否单调递增，如果是返回true否则false
        for i in range(1, len(values)):
            if values[i] > values[i - 1 ]:
                continue 
            else:
                return False 
        return True 

    def inOrder(self, node, vals):
        "中序遍历"
        if not node:
            return 
        
        self.inOrder(node.left, vals)
        vals.append(node.val)
        self.inOrder(node.right, vals)