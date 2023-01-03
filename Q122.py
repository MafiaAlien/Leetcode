from typing import List 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return prices[0]
        profit = 0
        
        for i in range(1, len(prices)):
            # 逐个分解步骤，只统计利润为正数的时候
            profit += max(prices[i] - prices[i-1], 0)
        
        return profit
