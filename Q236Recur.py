# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self._traversal(root, p, q)

    def _traversal(self, node, p, q):
        # 终止条件1
        if not node:
            return node 
        # 终止条件2: 某结点等于p或者q
        if node.val == p.val or node.val == q.val:
            return node 
        # 后序遍历: 因为是从底部到顶部，所以用后序遍历，如果是顶部到底部则用前序遍历：中左右
        # 左
        left = self._traversal(node.left, p, q)
        # 右
        right = self._traversal(node.right, p, q)
        # 中
        if left and right:
            # 通过终止条件2发现左右子树包含目标值，回溯公共节点
            return node 
        elif not left and right:
            # 如果左为空右不为空，则表示右子树找到了公共祖先，回溯return返回右子树结果
            return right 
        elif left and not right:
            # 同理左不为空右为空，则表示左子树中有目标值的公共祖先，通过左子树回溯到根节点
            return left 
        else:
            # 左右同时为空则没有满足p和q的目标值的公共祖先，所以一直返回None就可以
            return 
        

