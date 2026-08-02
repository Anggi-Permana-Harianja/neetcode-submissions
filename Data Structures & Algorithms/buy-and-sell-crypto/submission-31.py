class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_profit = 0
        max_profit = 0
        for i in range(1, len(prices)):
            curr_profit = max(0, curr_profit + prices[i] - prices[i-1])
            max_profit = max(max_profit, curr_profit)
        return max_profit