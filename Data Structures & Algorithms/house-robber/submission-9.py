class Solution:
    def dp(self, i):
        if i >= len(self.nums):
            return 0
        if self.memo[i] != -1:
            return self.memo[i]
        self.memo[i] = max(self.dp(i + 1), self.nums[i] + self.dp(i + 2))
        return self.memo[i]
        
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.memo = [-1] * len(nums)
        return self.dp(0)