class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = nums[0]
        for num in range(1, len(nums)):
            curr_sum = max(nums[num], curr_sum + nums[num])
            max_sum = max(max_sum, curr_sum)
        return max_sum
