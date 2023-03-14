from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        # 先将所有位置初始化为0，不考虑障碍
        dp = [[0 for _ in range(col)] for _ in range(row)]
        dp[0][0] = 0 if obstacleGrid[0][0] == 1 else 1
        if dp[0][0] == 0:
            return 0  # 如果第一个格子就是障碍，return 0
        # 第一行
        for i in range(1, col):
            # 如果遇到障碍物，剩下一行所有的路径都为0 堵死了
            if obstacleGrid[0][i] == 1:
                break 
            dp[0][i] = 1
        
        for j in range(1, row):
        # 第一列， 同理
            if obstacleGrid[j][0] == 1:
                break 
            dp[j][0] = 1 
        
        for i in range(1, row):
            for j in range(1, col):
                # 如果没有遇到障碍物，那么当前格子就是上面加左边
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]