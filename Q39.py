from typing import List 
class Solution:
    def __init__(self):
        self.res: List[List] = []
        self.combine: List[int] = []
        self.sum_: int = 0
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        self.res.clear()
        self.backtracking(candidates, target, 0) 
        return self.res 
    
    def backtracking(self, candidates: List[int], target: int, startIndex: int):
        if self.sum_ > target: # 剪枝操作，当前和大于目标直接return
            return 

        if self.sum_ == target: # 终止条件，如果和为目标值则将组合添加进结果集
            self.res.append(self.combine[:])
            return 
        
        for i in range(startIndex, len(candidates)):
            self.sum_ += candidates[i] # 加上当前值
            self.combine.append(candidates[i]) # 添加进临时组合
            self.backtracking(candidates, target, i) # 递归，此时因为可以添加重复值，所以选择i为当前startindex
            self.combine.pop() # 回溯操作，拿出前一个数
            self.sum_ -= candidates[i] # 回溯操作，减去前一个的值

if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    s = Solution()
    print(s.combinationSum(candidates, target))