from typing import *
class Solution:
    def __init__(self):
        self.res: List[List[int]] = []
        self.sub: List[int] = []

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.backTracking(nums, 0)
        return self.res 

    def backTracking(self, nums: List[int], startIndex: int):
        # 结果收集，因为子集是不需要终止条件的，循环完了就完了，但是要置于终止条件之前
        if len(self.sub) > 1:
            self.res.append(self.sub[:])
        
        # 终止条件，可要可不要
        if startIndex == len(nums):
            return 

        used = set() # 记录单层递归的用过的元素，不影响其他for循环
        for i in range(startIndex, len(nums)):
            if (self.sub and nums[i] < self.sub[-1]) or nums[i] in used: 
                # 确保元素单调递增 且是没用过的元素
                continue
   
            used.add(nums[i]) # 单层递归添加用过的元素
            self.sub.append(nums[i]) # 添加元素到子集
            self.backTracking(nums, i + 1) # 递归
            self.sub.pop() # 回溯
if __name__ == "__main__":
    s = Solution()
    print(s.findSubsequences([4,6,7,7]))