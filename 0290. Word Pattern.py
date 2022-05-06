class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        dictionary = dict()
        for i, p in enumerate(pattern):
            if p not in dictionary:
                dictionary[p] = words[i]
            else:
                if dictionary[p] != words[i]:
                    return False
        
        dictionary = dict()
        for i, p in enumerate(words):
            if p not in dictionary:
                dictionary[p] = pattern[i]
            else:
                if dictionary[p] != pattern[i]:
                    return False               
        return True
