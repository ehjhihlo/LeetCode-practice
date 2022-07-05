class Solution:
    def convertToBase7(self, num: int) -> str:
        res = ''
        if num == 0:
            return '0'
        sign = True
        if num < 0:
            sign = False
            num = -num
        while num != 0:
            res = str(num % 7) + res
            num = num // 7   
        if sign == False:
            res = '-' + res
            
        return res
