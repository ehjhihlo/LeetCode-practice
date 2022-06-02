class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_ran = Counter(ransomNote)
        dict_mag = Counter(magazine)
        
        for i, j in enumerate(ransomNote):
            if j not in dict_mag:
                return False
            if dict_ran[j] > dict_mag[j]:
                return False            
        return True
