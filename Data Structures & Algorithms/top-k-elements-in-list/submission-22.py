class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq_tbl = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, cnt in count.items():
            freq_tbl[cnt].append(num)
        res = []
        for i in range(len(freq_tbl) - 1, 0, -1):
            for num in freq_tbl[i]:
                res.append(num)
                if len(res) == k:
                    return res 