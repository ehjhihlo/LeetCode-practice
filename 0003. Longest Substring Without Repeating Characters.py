class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_list = []
        maxlen = 0
        for i in s:
            if i in str_list:
                str_list = str_list[str_list.index(i)+1:]
            
            str_list.append(i)
            maxlen = max(maxlen, len(str_list))
        return maxlen
