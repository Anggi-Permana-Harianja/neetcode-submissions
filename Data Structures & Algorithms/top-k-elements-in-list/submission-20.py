class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # for counter key value pair
        frq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, cnt in count.items():
            frq[cnt].append(num)

        res = []
        for i in range(len(frq) - 1, 0, -1):
            for num in frq[i]:
                res.append(num)
                if len(res) == k:
                    return res