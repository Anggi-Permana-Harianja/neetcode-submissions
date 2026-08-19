class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set_s, set_t = {}, {}
        for idx in range(len(s)):
            set_s[s[idx]] = 1 + set_s.get(s[idx], 0)
            set_t[t[idx]] = 1 + set_t.get(t[idx], 0)
        return set_s == set_t