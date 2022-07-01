# 用貪婪演算法解
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda boxType : boxType[1])[::-1]
        res = 0
        for i, j in boxTypes:
            if i < truckSize:
                truckSize-=i 
                res+=i*j
            else:
                res+=truckSize*j
                return res
        return res
