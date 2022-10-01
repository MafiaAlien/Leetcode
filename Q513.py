# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# iter
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 

        que = collections.deque()
        que.append(root)
        
        leftVal = 0
        
        while que:
            numOfNodes = len(que)
            isFirst = True 

            for _ in range(numOfNodes):
                node = que.popleft()
                if isFirst:
                    leftVal = node.val
                    isFirst = False 
                
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                    
        
        return leftVal

