class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        set_nums = set(nums)
        for num in set_nums:
            if num - 1 not in set_nums:
                curr_length = 1
                curr_num = num
                while curr_num + 1 in set_nums:
                    curr_length += 1
                    curr_num += 1
                longest = max(longest, curr_length)
        return longest