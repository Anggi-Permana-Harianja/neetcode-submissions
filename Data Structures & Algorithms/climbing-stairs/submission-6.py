class Solution:
    def dp(self, i):
        if i == 0 or i == 1:
            return 1
        if i in self.memo:
            return self.memo[i]
        self.memo[i] = self.dp(i - 1) + self.dp(i - 2)
        return self.memo[i]

    def climbStairs(self, n: int) -> int:
        self.memo = {}
        return self.dp(n)