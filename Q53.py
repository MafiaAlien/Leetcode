from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        result = float('-inf')  
        count = 0 # temp sum
        for i in range(len(nums)):
            # single pointer, add new value on current sum 
            count += nums[i]
            if count > result:
                # if the temp sum is larger than current max value, reset the max value by current value
                result = count
            if count <= 0:
                # if temp sum get 0, then drop prev temp sum and recalculate the sum of rest array;
                count = 0
        return result

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    s = Solution()
    print(s.maxSubArray(nums))