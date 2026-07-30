class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ = defaultdict(list)
        for str_ in strs:
            space = [0] * 26
            for char in str_:
                space[ord(char) - ord('a')] += 1
            dict_[tuple(space)].append(str_)
        return list(dict_.values())
