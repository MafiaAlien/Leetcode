# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        st = []
        curNode = root
        pre = None  
        minValue = float('inf')
        
        while curNode or st:
            if curNode:# push left children nodes to stack 
                st.append(curNode)
                curNode = curNode.left 
            else: # pop all left node in the stack and compare the value of curNode with that of preNode
                curNode = st.pop()
                if pre:
                    minValue = min(minValue, abs(curNode.val - pre.val))
                pre = curNode
                curNode = curNode.right
        return minValue


        