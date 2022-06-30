# Sol 1(TLE):
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        W = 1
        L = area
        diff = L-W
        for i in range(1,area+1):
            if area % i == 0:
                w = i
                l = area//i
                if l>=w and l-w<diff:
                    W = w
                    L = l
                    diff = l-w
        return [L,W]


# Sol 2:
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        n = int(math.sqrt(area))
        while area % n != 0:
            n = n-1
        return [int(area/n),n]
