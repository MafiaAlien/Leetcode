# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            node = TreeNode(val)
            return node 
        # 设定指针
        cur, parent = root, root  

        # while开始迭代，当前指针如果指向空节点，则pre的left或者right 为cur
        # cur = TreeNode(val)
        # 判断条件依然根据值的大小来决定左还是右

        while cur:
            # 指针遍历，然后保存父节点做最后添加新节点用
            parent = cur 
            if cur.val > val:
                cur = cur.left 
            else:
                cur = cur.right 
        # 赋值新节点
        node = TreeNode(val)
        # 根据父节点来决定是左子节点还是右子节点
        if val > parent.val:
            parent.right = node 
        else:
            parent.left = node 
        # 返回根
        return root 