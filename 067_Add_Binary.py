class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1, num2 = 0, 0
        for i in range(len(a)):
            if a[i] == '1':
                num1 += 2**int(len(a)-1-i)
        for j in range(len(b)):
            if b[j] == '1':
                num2 += 2**int(len(b)-1-j)
        output = bin(num1+num2)
        output = output[2:]
        return(output)
