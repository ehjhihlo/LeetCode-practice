class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row_length, col_length = len(grid), len(grid[0])
        peri = 0
        for i in range(row_length):
            for j in range(col_length):
                if grid[i][j] == 1:
                    if i==0 or grid[i-1][j]==0:
                        peri+=1
                    if i==row_length-1 or grid[i+1][j]==0:
                        peri+=1                    
                    if j==0 or grid[i][j-1]==0:
                        peri+=1
                    if j==col_length-1 or grid[i][j+1]==0:
                        peri+=1
        return peri
#整個row和col搜尋一次，看每塊陸地的前後左右有無陸地相連，如果是水的話就加1
