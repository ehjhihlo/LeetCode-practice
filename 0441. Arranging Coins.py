class Solution:
    def arrangeCoins(self, n: int) -> int:
        total= 0
        res = 0
        for i in range(2**31):
            total += i
            if total > n:
                res = i-1
                break
        return res
