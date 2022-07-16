class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[0]*n for _ in range(m)] for _ in range(maxMove+1)]
        steps = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for k in range(1, maxMove+1):
            for x in range(m):
                for y in range(n):
                    for step in steps:
                        new_x, new_y = x + step[0], y + step[1]
                        if new_x < 0 or new_y < 0 or new_x >=m or new_y >= n:
                            dp[k][x][y] += 1
                        else:
                            dp[k][x][y] = (dp[k][x][y] + dp[k-1][new_x][new_y]) % (10**9 + 7)
            
        return dp[maxMove][startRow][startColumn]
