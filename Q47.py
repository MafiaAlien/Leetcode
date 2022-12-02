from typing import List 

class Solution:
    def __init__(self):
        self.res: List[List[int]] = []
        self.path: List[int] = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        nums.sort()
        self._backTracking(nums, used)
        return self.res 
    
    def _backTracking(self, nums: List[int], used: List[bool]) -> None:
        if len(self.path) == len(nums):
            self.res.append(self.path[:])
            return 
    
        for i in range(0, len(nums)):
            if nums[i-1] == nums[i] and i > 0 and used[i-1] == False:
                # 树层去重，避免选不同元素相同值
                continue
            
            if not used[i]:
                # 树枝去重，避免取重复元素
                used[i] = True 
                self.path.append(nums[i])
                self._backTracking(nums, used)
                self.path.pop()
                used[i] = False 

if __name__ == "__main__":
    s = Solution()
    print(s.permuteUnique([1,2,2,3]))