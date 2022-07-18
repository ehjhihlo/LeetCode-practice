class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:     
        res = 0
        # prefix sum
        for row in matrix:
            for i in range(1,len(matrix[0])):
                row[i] += row[i-1]
                
        for col in range(len(matrix[0])):
            for j in range(col, len(matrix[0])):
                prefix_count = Counter({0:1})
                sum_ = 0
                for i in range(len(matrix)):
                    if col > 0:
                        sum_ -= matrix[i][col-1]
                    sum_ += matrix[i][j]
                    res += prefix_count[sum_ - target]
                    prefix_count[sum_] += 1
        
        return res
