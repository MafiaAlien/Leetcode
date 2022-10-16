# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        pre = None # 前指针指向前结点
        maxCnt = 0 # 最高频次
        stack = []
        curNode = root 
        while curNode or stack:
            if curNode:# 中序遍历 左侧结点压入栈
                stack.append(curNode)
                curNode = curNode.left 
            else:
                curNode = stack.pop() # 中：处理结点
                
                if not pre: # 如果是第一个结点没有前结点
                    curCnt = 1 
                elif curNode.val == pre.val: # 如果前结点与现结点值一样，则频次加一
                    curCnt += 1 
                else: # 如果前结点与现结点值不一样， 则频次归一
                    curCnt = 1
                
                if curCnt == maxCnt: # 对比频次如果等于当前最大频次 则将结点加入结果集
                    res.append(curNode.val)
                if curCnt > maxCnt: # 如果现频次高于最大频次，则清空结果集并将新的现结点加入结果集
                    maxCnt = curCnt
                    res.clear()
                    res.append(curNode.val)
                
                pre = curNode
                curNode = curNode.right # 右
        return res 
