# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]):
        # 递归终止条件，前序数组没有value
        if not preorder:
            return 

        # 找到根节点的值，前序为index==0的value
        rootValue = preorder[0]
        root = TreeNode(val=rootValue)
        # 设置切割点
        i = inorder.index(rootValue)
        # 设置中序数组左区间和右区间
        inorderLeft = inorder[:i]
        inorderRight = inorder[i + 1:]
        
        # 设置前序数组左区间和右区间,注意这里根节点是第一个值，所以后面的长度应该加上1
        preorderLeft = preorder[1: 1 + len(inorderLeft)]
        preorderRight = preorder[1 + len(inorderLeft):]
        
        # 递归处理剩余叶子节点
        root.left = self.buildTree(preorderLeft, inorderLeft)
        root.right = self.buildTree(preorderRight, inorderRight)
        # 返回结果
        return root

if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    s = Solution()
    print(s.buildTree(preorder,inorder))