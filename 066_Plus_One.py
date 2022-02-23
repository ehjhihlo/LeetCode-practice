class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        output = []
        for i in range(len(digits)):
            number += int(digits[i])*10**(len(digits)-1-i)
        string = str(number+1)
        for s in range(len(string)):
            output.append(int(string[s]))
        return output
