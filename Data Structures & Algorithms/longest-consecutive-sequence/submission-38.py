class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        map_ = defaultdict(int)
        for i in range(len(nums)):
            curr_ = nums[i]
            if not map_[curr_]:
                map_[curr_] = map_[curr_ + 1] + map_[curr_ - 1] + 1
                map_[curr_ - map_[curr_ - 1]] = map_[curr_]
                map_[curr_ + map_[curr_ + 1]] = map_[curr_]
            res = max(res, map_[curr_])
        return res