class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq_tbl = [[] for i in range(len(nums) + 1)]
        map_ = {}
        for i in range(len(nums)):
            map_[nums[i]] = 1 + map_.get(nums[i], 0)
        for value, count in map_.items():
            freq_tbl[count].append(value)
        for i in range(len(freq_tbl) - 1, 0, -1):
            for num in freq_tbl[i]:
                res.append(num)
                if len(res) == k:
                    return res