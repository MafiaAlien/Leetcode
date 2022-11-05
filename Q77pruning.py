class Solution:
    def __init__(self):
        self.path = [] # retore temp path
        self.res = [] # restore results
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        startIndex = 1 # 确认起始点，避免组合重复（组合是无关顺序的）
        self.backtracking(n,k,startIndex)
        return self.res # 返回结果集
       
    def backtracking(self, n:int, k:int, startIndex:int):
        # end of recur, if length of path is equal to k, save the path in the res list 
        if len(self.path) == k:
            self.res.append(self.path[:])
            return 
        # 横向遍历1 -> 4查找组合，i在这里是startindex 
        # 注意：第二个 + 1 前为剪纸操作， 如果当前for循环的开始位置已经小于我们要求的k的长度，就没必要遍历了
        for i in range(startIndex, (n - (k - len(self.path)) + 1) + 1):
            self.path.append(i) # 起始值添加进path
            self.backtracking(n, k, i + 1) # 递归纵向查找组合
            self.path.pop() # 回溯过程，将满足条件的path前一元素弹出继续查找其他元素

        
        