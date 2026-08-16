class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = {}
        left = 0
        for idx, char in enumerate(s):
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            else:
                res = max(res, idx - left + 1)
            seen[char] = idx
        return res
