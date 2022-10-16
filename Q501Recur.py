# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        # 几个全局变量
        self.pre = None
        self.maxCnt = 0 
        self.stack = []
        self.res = []
        self.cnt = 0
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None   
        self.searchBST(root)
        return self.res 

    def searchBST(self, node):
        #终止条件
        if not node:
            return 
        # 中序遍历
        # 左
        self.searchBST(node.left)
        # 中：单层处理结点逻辑
        if not self.pre:
            # 如果第一次编辑没有pre结点
            self.cnt = 1 
        elif self.pre.val == node.val:
            # 如果前结点的值等于后一结点的值 则当前值频次加1
            self.cnt += 1 
        else:
            # 如果前结点值不等于现结点值，则频次归一
            self.cnt = 1 

        if self.cnt == self.maxCnt:
            # 如果频次等于最大频次，则将当前结点加入结果数组
            self.res.append(node.val)
        if self.cnt > self.maxCnt:
            # 如果当前频次大于最大频次，更新最大频次等于当前频次并且清空结果集，并且将当前结点加入结果集
            self.maxCnt = self.cnt 
            self.res.clear()
            self.res.append(node.val)

        self.pre = node 
        # 右
        self.searchBST(node.right)