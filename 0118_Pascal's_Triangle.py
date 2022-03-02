class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        if not numRows:
            return []
        for i in range(numRows):
            res.append([1]*(i+1))
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res
