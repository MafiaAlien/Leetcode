from typing import List 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 

        slow, fast = 0, 1
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                # 关键是判断快慢指针的差是大于1的，以便直接跳过重复值
                if fast - slow > 1:
                    # 改变下一位的值是为了确保当前值如果重复至少保留1个
                    nums[slow + 1] = nums[fast]
                slow += 1
            fast += 1
            

        return slow + 1
    
if __name__ == '__main__':
    s = Solution()
    assert print(s.removeDuplicates([1, 2, 3, 3, 4, 4, 5, 6, 7]))
    print('pass')