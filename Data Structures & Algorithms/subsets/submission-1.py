class Solution:
    def dfs(self, i):
        if i >= len(self.nums):
            self.res.append(self.subset.copy())
            return 
        self.subset.append(self.nums[i])
        self.dfs(i + 1)
        self.subset.pop()
        self.dfs(i + 1)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.res = []
        self.subset = []
        self.dfs(0)
        return self.res