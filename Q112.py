# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False 
        
        total = targetSum - root.val
        return self._getSum(root, total)

    def _getSum(self, node, total):
        # 终止条件为到达叶子结点，随后返回一条路径的总和 如果total减成0了说明满足一条路径和为target
        if not node.left and not node.right and total ==0:
            return True
            
        if node.left:
            total -= node.left.val # 减去值
            # 因为递归函数有结果返回，所以这里传递True返回根节点，只要有一条满足true就传递返回结果
            if self._getSum(node.left, total):
                return True
            total += node.left.val # 回溯过程，减了的要加回来
            
        if node.right:
            # 同上同理
            total -= node.right.val
            if self._getSum(node.right, total):
                return True
            total += node.right.val 
        
        #递归完毕没找到合适路径，返回false
        return False
        

# Iteration
class solution1:
    def haspathsum(self, root: treenode, targetsum: int) -> bool:
        if not root: 
            return False

        stack = []  # [(当前节点，路径数值), ...]
        stack.append((root, root.val))

        while stack: 
            cur_node, path_sum = stack.pop() # 因为每个节点都记录了当前节点的sum值，相当于回溯

            if not cur_node.left and not cur_node.right and path_sum == targetsum: 
                return True

            if cur_node.right: 
                stack.append((cur_node.right, path_sum + cur_node.right.val))    

            if cur_node.left: 
                stack.append((cur_node.left, path_sum + cur_node.left.val))

        return False