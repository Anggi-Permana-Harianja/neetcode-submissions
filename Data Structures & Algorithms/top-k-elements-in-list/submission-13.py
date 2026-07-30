class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       count = Counter(nums)
       sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
       return [num for num, _ in sorted_count[:k]]