class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        space_ = [0] * 26
        for i in range(0, len(s)):
            space_[ord(s[i]) - ord('a')] += 1
            space_[ord(t[i]) - ord('a')] -= 1
        for i in space_:
            if i != 0:
                return False
        return True