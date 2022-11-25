from typing import *

class Solution:
    def __init__(self):
        self.res: List[List[int]] = []
        self.sub: List[int] = []
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        used = [False] * len(nums)
        self._backTracking(nums, used, 0)
        return self.res

    def _backTracking(self, nums: List[int], used: List[bool], startIndex: int):
        self.res.append(self.sub[:])  # 收集结果
        
        if startIndex >= len(nums): # 终止条件
            return 

        for i in range(startIndex, len(nums)):
            if nums[i-1] == nums[i] and i > startIndex and used[i] == False :
                # 去重
                continue 
        
            self.sub.append(nums[i])
            used[i] = True
            self._backTracking(nums, used, i + 1)
            self.sub.pop()
            used[i] = False 

if __name__ == "__main__":
    nums = [1,2,2,3,4,5,6,7,7]
    s = Solution()
    print(s.subsetsWithDup(nums))