class Solution:
    def helper(self, nums):
        memo = [-1] * len(nums)
        def dp(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dp(i + 1), nums[i] + dp(i + 2))
            return memo[i]
        return dp(0)
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1 : ]), self.helper(nums[ : -1]))