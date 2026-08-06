class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        left = 0
        res = 0
        max_count = 0
        for i, char in enumerate(s):
            curr_char = char
            seen[curr_char] = 1 + seen.get(curr_char, 0)
            max_count = max(max_count, seen[curr_char])
            if (i - left + 1) - max_count > k:
                seen[s[left]] -= 1
                left += 1
            res = max(res, i - left + 1)
        return res