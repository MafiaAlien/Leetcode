# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0   
        
        st = []
        st.append(root)
        total = 0
    
        while st:
            node = st.pop()
            # 判断是否是左叶子结点，左子节点没有子节点，即终止条件
            if node.left and not node.left.left and not node.left.right:
                total += node.left.val 
            # 后序遍历，先将右子树压入栈，再将左子树压入栈，循环开始的时候弹出
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        
        return total
        