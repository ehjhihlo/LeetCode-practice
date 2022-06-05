class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict_ = Counter(s)
        res = 0
        m = 0
        for i in dict_.values():
            if i % 2 == 0:
                res += i
            else:
                res += i - 1
                m = 1
        return res + m
