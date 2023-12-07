from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      n: int = len(nums)
      ans: List[int] = [0] * n

      # pre product of current number 
      ans[0] = 1
      for i in range(1, n):
        # current num multiply by previous ans(the product)
        ans[i] = nums[i - 1] * ans[i - 1]

      # post product, just need a variable to record cum product
      # initialize 1 
      R = 1
      # begin from the the tail 
      for i in range(n-1, -1 ,-1):
        ans[i] = ans[i] * R 
        # R cum with current number
        R *= nums[i]
      
      return ans
    
def main():
   s = Solution()
   nums = [7, 8, 4, 6, 5]
   return s.productExceptSelf(nums)


if __name__ == "__main__":
   print(main())


        