from typing import List
class Solution:
    def numTrees(self, n: int) -> int:
        # 确定动规数组， 下表的含义为当前节点总数总共可以构成几颗树
        dp: List[int] = [0] * (n + 1)

        # 确定初始化
        dp[0], dp[1] = 1, 1

        # 确定递推条件和遍历顺序：通过画图可以知道dp[3] 为 0个节点乘以1个节点加上0个节点乘以2个节点加上1个节点乘以两个节点
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[ i - j]

        return dp[-1]

    
if __name__ == '__main__':
    n = 5
    s = Solution()
    print(s.numTrees(n))