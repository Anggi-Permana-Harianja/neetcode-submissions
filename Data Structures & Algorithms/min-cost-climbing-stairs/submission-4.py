class Solution:
    def dp(self, i):
        if i >= len(self.cost):
            return 0
        if self.memo[i] != -1:
            return self.memo[i]
        self.memo[i] = self.cost[i] + min(self.dp(i + 1), self.dp(i + 2))
        return self.memo[i]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = cost
        self.memo = [-1] * len(cost)
        return min(self.dp(0), self.dp(1))