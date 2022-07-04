class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        list1 = 'qwertyuiopQWERTYUIOP'
        list2 = 'asdfghjklASDFGHJKL'
        list3 = 'zxcvbnmZXCVBNM'
        res = []
        
        for word in words:
            row = 0
            count1, count2, count3 = 0, 0, 0
            for c in word:
                if c in list1:
                    count1=1
                if c in list2:
                    count2=1
                if c in list3:
                    count3=1
            row = count1 + count2 + count3
            if row == 1:
                res.append(word)
        
        return res
