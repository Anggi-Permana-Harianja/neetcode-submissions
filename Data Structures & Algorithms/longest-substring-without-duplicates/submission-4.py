class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = {}
        res = 0
        for right in range(len(s)):
            curr_char = s[right]
            if curr_char in seen and seen[curr_char] >= left:
                left = seen[curr_char] + 1
            else:
                res = max(res, right - left + 1)
            seen[curr_char] = right
        return res