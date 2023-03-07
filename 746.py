from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 确定dp数组
        dp: List[int] = [0] * (len(cost) + 1)
        # 初始化， 不走就没有cost，所以都是0 ，而且起点可以选择从 第0或者第1开始
        dp[0]: int = 0
        dp[1]: int = 0
        # 遍历顺序， 后一个状态是前一个状态来的，所以从前向后iter
        for i in range(2, len(cost) + 1):
            # 递推条件，选择两步内cost少的那一步，来推后一步
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[-1]