class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]
            curr_profit = max(0, curr_profit + profit)
            max_profit = max(max_profit, curr_profit)
        return max_profit