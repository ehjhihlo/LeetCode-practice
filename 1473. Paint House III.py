# from: https://zhuanlan.zhihu.com/p/414732273

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        houses = [i-1 for i in houses]
        for i in range(m):
            f = [[None]*n for _ in range(target+1)]
            if i == 0:
                if houses[i] == -1:
                    for k in range(n):
                        f[1][k] = cost[0][k]
                else:
                    f[1][houses[i]] = 0
            
            else:
                for j in range(1, target+1):
                    if j > i+1:
                        continue
                    if houses[i] == -1:
                        for k in range(n):
                            if g[j][k] is not None and f[j][k] is None:
                                f[j][k] = g[j][k] + cost[i][k]
                            for p in range(n):
                                if p!= k:
                                    if g[j-1][p] is not None and (f[j][k] is None or g[j-1][p] + cost[i][k] < f[j][k]):
                                        f[j][k] = g[j-1][p] + cost[i][k]
                    
                    else:
                        for k in range(n):
                            if k == houses[i]:
                                if g[j][k] is not None and (f[j][houses[i]] is None or g[j][k] < f[j][houses[i]]):
                                    f[j][houses[i]] = g[j][k]
                            else:
                                if g[j-1][k] is not None and (f[j][houses[i]] is None or g[j-1][k] < f[j][houses[i]]):
                                    f[j][houses[i]] = g[j-1][k]                                
        
            g = f[:]
        
        res = None
        
        for k in range(n):
            if f[-1][k] is not None and (res is None or res > f[-1][k]):
                res = f[-1][k]
        
        if res is None:
            res = -1
        
        return res
