class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_ = {}
        for i in nums:
            if i in dict_:
                return True
            dict_[i] = 0

        return False