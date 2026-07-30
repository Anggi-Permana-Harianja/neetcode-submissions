class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_length = 0
        for num in set_nums:
            if num - 1 not in set_nums:
                curr_length = 1
                curr_num = num
                while curr_num + 1 in set_nums:
                    curr_num += 1
                    curr_length += 1
                max_length = max(max_length, curr_length)
        return max_length