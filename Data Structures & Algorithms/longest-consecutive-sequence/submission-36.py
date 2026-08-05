class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        map_ = defaultdict(int)
        for i in range(len(nums)):
            if not map_[nums[i]]:
                map_[nums[i]] = map_[nums[i] - 1] + map_[nums[i] + 1] + 1
                map_[nums[i] - map_[nums[i] - 1]] = map_[nums[i]]
                map_[nums[i] + map_[nums[i] + 1]] = map_[nums[i]]
            res = max(res, map_[nums[i]])
        return res