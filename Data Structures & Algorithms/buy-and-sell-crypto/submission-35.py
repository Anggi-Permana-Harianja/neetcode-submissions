class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_profit, max_profit = 0, 0
        left, right = 0, len(prices) - 1
        for i in range(1, len(prices)):
            curr_profit = max(0, curr_profit + prices[i] - prices[i-1])
            max_profit = max(max_profit, curr_profit)
        return max_profit
