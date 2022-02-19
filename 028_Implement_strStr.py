class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            res = 0
        if haystack == '' and needle != '':
            res = -1
        if len(needle) > len(haystack):
            res = -1 
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                res = i
                break
            else:
                res = -1
        return res
