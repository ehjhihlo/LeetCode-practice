class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        gs, ss = 0, 0
        while gs < len(g) and ss < len(s):
            if g[gs] <= s[ss]:
                gs+=1
            ss+=1
        return gs
