class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # sort the array reversely by abs value 
        nums = sorted(nums, key=abs, reverse=True)

        for i in range(len(nums)):
            # change the nagative num to positive 
            if k > 0 and nums[i] < 0:
                nums[i] *= -1
                k -= 1
        
        # k still has rest, then change the minimum number to clear k steps
        if k > 0: 
            nums[-1] *= (-1) ** k 
        return sum(nums)