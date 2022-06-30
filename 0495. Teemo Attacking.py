class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries)==0:
            return 0
        if len(timeSeries)==1:
            return duration
        res = duration
        for i in range(1,len(timeSeries)):
            res+=min(timeSeries[i]-timeSeries[i-1],duration)
        return res
