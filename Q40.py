from typing import List 

class Solution:
    def __init__(self):
        self.res: List[List] = []
        self.combine: List = []
        self.sum_: int = 0
        

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:        
        candidates.sort()
        self.used_list = [False] * len(candidates)  # 标记哪个元素我们用过，这一步很关键
        self.backtracking(candidates, target, 0)
        return self.res
    
    def backtracking(self, candidates: List[int], target: int, startIndex: int):
        if self.sum_ > target: # 同前面题一样，剪枝操作，如果和大于目标值则返回
            return 

        if self.sum_ == target: # 终止条件，如果和满足就添加入结果集
            self.res.append(self.combine[:])
            return 
        
        for i in range(startIndex, len(candidates)):
            if candidates[i] == candidates[i-1] and i > 0 and self.used_list[i-1] == False:
                # 同层去重，后一个candidate等于前一个candidate且前一个candidate没被用过则跳过
                continue
            
            self.sum_ += candidates[i]
            self.combine.append(candidates[i])
            self.used_list[i] = True
            self.backtracking(candidates, target, i + 1)
            self.used_list[i] = False # 回溯1
            self.sum_ -= candidates[i] # 回溯2
            self.combine.pop() # 回溯3
            
if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    target = 8
    s = Solution()
    print(s.combinationSum2(candidates, target))