class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        seen = {}
        left = 0
        max_count_seen = 0
        for idx, char in enumerate(s):
            seen[char] = 1 + seen.get(char, 0)
            max_count_seen = max(max_count_seen, seen[char])
            if (idx - left + 1) - max_count_seen > k:
                seen[s[left]] -= 1
                left += 1
            res = max(res, idx - left + 1)
        return res