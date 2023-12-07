from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        因为一个元素最多出现两次，所以只需要用双指针检查当前指针（快指针）和前三元素（慢指针-2）元素是否相同即可
        """
        if len(nums) <= 2:
            return len(nums)

        fast: int = 2
        slow: int = 2
        while fast < len(nums):

            if nums[fast] != nums[slow-2]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1


        return slow 
