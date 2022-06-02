class Solution:
    def firstUniqChar(self, s: str) -> int:
        str_dict = Counter(s)
        
        for i, j in enumerate(s):
            if str_dict[j] <= 1:
                return i
        return -1
