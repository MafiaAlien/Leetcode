# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 指针操作
        curNode = root
        
        # 二叉搜索树是一个有序树：

        #     若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
        #     若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
        #     它的左、右子树也分别为二叉搜索树
        while curNode:
            if curNode.val == val:
                return curNode
            elif curNode.val > val:
                # 如果当前值大于目标值，则向左遍历
                curNode = curNode.left 
            else:
                # 反之向右
                curNode = curNode.right 
        
        return 