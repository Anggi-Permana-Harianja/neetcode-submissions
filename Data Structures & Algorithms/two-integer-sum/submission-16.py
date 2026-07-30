class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_ = dict()
        for idx, num in enumerate(nums):
            remain = target - num
            if remain in seen_:
                return [seen_[remain], idx]
            seen_[num] = idx
        return []