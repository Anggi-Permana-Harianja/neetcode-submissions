class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        seen = {} # char: idx
        for idx, val in enumerate(s):
            if val in seen and seen[val] >= left:
                left = seen[val] + 1
            else:
                res = max(res, idx - left + 1)
            seen[val] = idx
        return res