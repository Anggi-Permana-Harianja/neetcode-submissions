class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_, max_ = nums[0], nums[0]
        for i in range(1, len(nums)):
            curr_ = max(nums[i], curr_ + nums[i])
            max_ = max(max_, curr_)
        return max_