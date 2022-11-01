# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 终止条件
        if not nums:
            return None 
        
        # 类似于leetcode 106
        # 中序遍历 左中右 找到数组中节点当作根节点
        mid = len(nums) // 2

        # 单层逻辑：划分左子树和右子树
        # 注意这里不取mid是因为mid是当前节点的val
        left_region = nums[ : mid]
        right_region = nums[mid+1 : ]
        
        # 构造节点
        root = TreeNode(nums[mid]) 
        
        # 递归处理左右区间直到数组为空
        root.left = self.sortedArrayToBST(left_region)
        root.right = self.sortedArrayToBST(right_region)

        # 返回构造好的根节点
        return root 