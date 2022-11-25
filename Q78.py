from typing import List 

class Solution:
    def __init__(self):
        self.res: List[List[int]] = []
        self.sub: List[int] = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self._backTracking(nums, 0)
        return self.res

    def _backTracking(self, nums: List[int], startIndex: int):
        self.res.append(self.sub[:]) # 收集结果
        
        if startIndex >= len(nums):
            # 终止条件
            return 
        
        for i in range(startIndex, len(nums)):
            self.sub.append(nums[i]) # 添加结果集
            self._backTracking(nums, i + 1) # 递归
            self.sub.pop() # 回溯


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    s = Solution()
    print(s.subsets(nums))