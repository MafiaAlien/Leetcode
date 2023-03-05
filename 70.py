from typing import List 
class Solution:
    # 实际上是另外一种fib数列
    def climbStairs(self, n: int) -> int:
        dp: List[int] = [0] * (n + 1) 
        dp[0] = 1 
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[-1]
    
if __name__ == " __main__":
    s = Solution()
    print(s.climbStairs(n=6))