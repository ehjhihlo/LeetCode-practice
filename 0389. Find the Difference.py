class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict_s = Counter(s)
        dict_t = Counter(t)
        
        for i, j in enumerate(t):
            if j not in dict_s:
                return j
            elif dict_t[j] != dict_s[j]:
                return j
