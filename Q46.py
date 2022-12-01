from typing import List 
class Solution:
    def __init__(self):
        self.res: List[List[int]] = []
        self.path: List[int] = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        self.backTracking(nums, used)
        return self.res

    def backTracking(self, nums: List[int], used: List[bool]):
        if len(self.path) == len(nums):
            # 终止条件
            self.res.append(self.path[:])
            return 

        for i in range(0, len(nums)):
            # 从0开始取是因为这是排列，不需要startindex控制起始值，和组合不同
            if used[i] == True:
                # 标记当前数字是否被用过（递归中），树枝方向标记
                continue 
            
            used[i] = True 
            self.path.append(nums[i])
            self.backTracking(nums, used)
            used[i] = False # 回溯1
            self.path.pop() # 回溯2

if __name__ == "__main__":
    s = Solution()
    print(s.permute([1,2,3,4,5]))