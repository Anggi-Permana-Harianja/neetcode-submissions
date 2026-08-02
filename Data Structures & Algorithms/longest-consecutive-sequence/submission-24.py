class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map_ = defaultdict(int)
        res = 0
        for num in nums:
            if not map_[num]:
                map_[num] = map_[num - 1] + map_[num + 1] + 1
                map_[num - map_[num - 1]] = map_[num]
                map_[num + map_[num + 1]] = map_[num]
            res = max(res, map_[num])
        return res