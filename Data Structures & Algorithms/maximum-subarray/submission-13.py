class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_profit, max_profit = nums[0], nums[0]
        for i in range(1, len(nums)):
            curr_profit = max(nums[i], curr_profit + nums[i])
            max_profit = max(max_profit, curr_profit)
        return max_profit