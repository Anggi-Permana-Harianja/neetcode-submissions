class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map_ = {}
        left = 0
        curr_max_length = 0
        res = 0
        for right in range(len(s)):
            map_[s[right]] = 1 + map_.get(s[right], 0)
            curr_max_length = max(curr_max_length, map_[s[right]])
            while (right - left + 1) - curr_max_length > k:
                map_[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res