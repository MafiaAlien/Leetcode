from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        
        cover:int = 0 # 当前能够覆盖到的范围，检查是否最终能覆盖到终点
        i:int = 0 # 每次的步长
        while i <= cover:
            cover = max(nums[i] + i, cover)
            if cover >= len(nums) - 1: 
                return True 
            i += 1
        else:
            return False  

if __name__ == "__main__":
    pass 