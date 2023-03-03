from typing import List 
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        # define dp arrary
        dp: List[int] = [0] * (n + 1)  
        # initialize beginning values 
        dp[0], dp[1] = 0, 1 
        # iter condition 
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        # return result
        return dp[n]
    

if __name__ == "__main__":
    s = Solution()
    print(s.fib(10))