class Solution:
    def dp(self, n):
        if n in self.memo:
            return self.memo[n]
        if n == 1 or n == 0:
            return 1
        self.memo[n] = self.dp(n - 1) + self.dp(n - 2)
        return self.memo[n]

    def climbStairs(self, n: int) -> int:
        self.memo = {}
        return self.dp(n)