class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n_lens = len(nums)
        res = [1] * n_lens

        prefix = 1
        for i in range(n_lens):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n_lens - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res