from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        min_price = prices[0]
        res : int = 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] > (min_price + fee):
                res += prices[i] - (min_price + fee)
                min_price = prices[i] - fee 
            else:
                continue
        return res 
    
if __name__ == "__main__":
    prices = [1,3,2,8,4,9] 
    fee = 2
    s = Solution()
    print(s.maxProfit(prices=prices, fee=fee))