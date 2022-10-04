# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return 
        
        # 通过后序数组最后一个结点找到根节点
        rootValue = postorder[-1] 
        # 设置根节点
        root = TreeNode(val = rootValue)  
        
        # 设置切割点：在中序数组中寻找根节点当作切割点
        i = inorder.index(rootValue)
        
        # 通过根节点当作切割点切中序数组：左中序，右中序
        inLeftSubTree = inorder[:i]
        inRightSubTree = inorder[i + 1:] # 确保根节点不被取

        # 同上切后序数组(注意边界问题)：
        postLeftSubTree = postorder[:len(inLeftSubTree)]
        postRightSubTree = postorder[len(inLeftSubTree): len(postorder) - 1 ] # 保留中节点不被取所以这减去1

        # 递归处理左区间： rootLeft = traversal(左中序，左后序)
        root.left = self.buildTree(inLeftSubTree, postLeftSubTree)
        # 递归处理右区间： rootRight = traveral(右中序，右后序)
        root.right = self.buildTree(inRightSubTree, postRightSubTree)
        return root 