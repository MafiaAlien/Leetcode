from typing import List
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        curDiff: int = 0
        preDiff: int = 0 
        res: int = 1
        for i in range(len(nums)-1):
            curDiff = nums[i + 1] - nums[i]

            if curDiff * preDiff <= 0 and curDiff !=0:
                res += 1 
                preDiff = curDiff

        return res 

if __name__ == "__main__":
    nums = [1,17,5,10,13,15,10,5,16,8]
    s = Solution()
    print(s.wiggleMaxLength(nums))