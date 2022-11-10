from typing import List

class Solution:
    def __init__(self):
        self.sum_ = 0
        self.res = []
        self.nums = []
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        startIndex = 1
        self.backtracking(k, n, startIndex) 
        return self.res

    def backtracking(self, k:int, n:int, startIndex:int):
        if self.sum_ > n: # 剪枝操作
            return 
        
        if len(self.nums) == k: # 终止条件，长度为k和为n则满足
            if self.sum_ == n: # 如果sum满足target则返回当前组合
                self.res.append(self.nums[:])
            return 
            
        for i in range(startIndex, 10 - (k - len(self.nums)) + 1): 
            # 附带的剪枝操作，如果剩余长度小于K则不iter n -(k - len(cur_path)) +1
            self.sum_ += i
            self.nums.append(i)
            self.backtracking(k, n, i + 1)
            # 回溯操作
            self.nums.pop()
            self.sum_ -= i

if __name__ == "__main__":
    k = 3 
    n = 9
    s = Solution()
    print(s.combinationSum3(k, n))