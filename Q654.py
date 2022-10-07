# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # end of recuisive 
        if len(nums) == 1:
            return TreeNode(val=nums[0])

        # find out max value in the nums (mid) of preorder
        rootValue = max(nums)
        root = TreeNode(val=rootValue)
        spliter = nums.index(rootValue)

        # define left sub array and right sub array by idx 
        # make sure length of nums is larger than 0
        # recursively create binarytree 
        if spliter > 0:
            leftSubArray = nums[: spliter] # left of preorder
            root.left = self.constructMaximumBinaryTree(leftSubArray)
        # make right sub array has elements
        if  spliter < len(nums) - 1:   
            rightSubArray = nums[spliter + 1: ] # right of preorder 
            root.right = self.constructMaximumBinaryTree(rightSubArray)
        
        # return tree
        return root