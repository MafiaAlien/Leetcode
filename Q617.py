# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # recur end
        # if any one of the root1 or root2 is None, then the other not none value will be return
        # if both root1 and root2 are None, the func will return None 
        if not root1:
            return root2
        if not root2:
            return root1 
        # the if expression above makes sure that both root1 and root2 are not None value 
        
        # preorder: mid merge the value 
        root1.val += root2.val
        # left 
        root1.left = self.mergeTrees(root1.left, root2.left)
        # right
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1