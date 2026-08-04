class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        map_ = {}
        max_curr_len = 0
        res = 0
        for right in range(len(s)):
            map_[s[right]] = 1 + map_.get(s[right], 0)
            max_curr_len = max(max_curr_len, map_[s[right]])
            while (right - left + 1) - max_curr_len > k:
                map_[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res