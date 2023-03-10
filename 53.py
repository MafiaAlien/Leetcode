from typing import List
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 初始化dp数组 最上层和最左边的路径只有1个方法达到
        dp: List[List] = [[1 for i in range(n)] for j in range(m)]
        # 确定遍历顺序，左->右 上->下
        for i in range(1, m):
            for j in range(1, n):
                # 当前格子到达的方法数为上面格子方法数加上左边格子的方法数
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
        return dp[m-1][n-1]