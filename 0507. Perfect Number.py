import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        i = 1
        div_list = []
        while i < math.sqrt(num):
            if i <= 1:
                div_list.append(1)
            else:
                if num % i == 0:
                    if num / i == i:
                        div_list.append(i)
                    div_list.append(i)
                    div_list.append(num/i)
            i+=1

        if sum(div_list) == num:
            return True
        return False
