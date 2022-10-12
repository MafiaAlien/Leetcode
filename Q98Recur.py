# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 双指针前后比较，不用单独划数组存储所有节点
        stack = []
        cur = root
        pre = None
        while cur or stack:
            # 将左子树叶子结点全部压入栈，直接到达左子树低端
            if cur:
                stack.append(cur)   
                cur = cur.left 
            else:
                # 从栈中弹出左子树的结点，有左节点则压入栈
                cur = stack.pop()  
                if pre and cur.val <= pre.val:
                    return False 
                pre = cur
                cur = cur.right 
        return True 


