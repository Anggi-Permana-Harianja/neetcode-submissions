class Solution:
    def dp(self, i):
        if i == self.n:
            return 1
        if i > self.n:
            return 0
        if self.memo[i] != -1:
            return self.memo[i]
        self.memo[i] = self.dp(i + 1) + self.dp(i + 2)
        return self.memo[i]

    def climbStairs(self, n: int) -> int:
        self.n = n
        self.memo = [-1] * (n + 1)
        return self.dp(0)