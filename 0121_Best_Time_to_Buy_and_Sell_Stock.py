class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 10001
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            if profit < (prices[i] - buy):
                profit = prices[i] - buy
        return profit
