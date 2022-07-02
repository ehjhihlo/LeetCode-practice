class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mod = 1000000007
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)
        horizontalCuts.insert(0,0)
        horizontalCuts.append(h)
        verticalCuts.insert(0,0)
        verticalCuts.append(w)
        
        max_horizontal = 0
        max_vertical = 0
        for i in range(1,len(horizontalCuts)):
            diff = horizontalCuts[i] - horizontalCuts[i-1]
            max_horizontal = max(max_horizontal, diff)
        for i in range(1,len(verticalCuts)):
            diff = verticalCuts[i] - verticalCuts[i-1]
            max_vertical = max(max_vertical, diff)
           
        max_area = (int)(max_horizontal*max_vertical % mod)
        return max_area
