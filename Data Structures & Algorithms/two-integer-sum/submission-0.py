class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remain = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in remain:
                return [remain[diff], idx]
            remain[num] = idx