def climbStairs(n, cache):
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 3
        if n in cache:
            return cache[n]
        cache[n] = climbStairs(n-2, cache)+climbStairs(n-1, cache)
        return cache[n]

class Solution:
    def climbStairs(self, n: int) -> int:
        return climbStairs(n, {})
