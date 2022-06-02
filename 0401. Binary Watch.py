class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        self.dfs(turnedOn, 0, res)
        return res
    
    def dfs(self, turnedOn, hours, res):
        if hours > turnedOn:
            return
        for h in combinations([1,2,4,8],hours):
            hrs = sum(h)
            if hrs >= 12:
                continue
            for m in combinations([1,2,4,8,16,32], turnedOn-hours):
                mins = sum(m)
                if mins >= 60:
                    continue
                res.append('%d:%02d' % (hrs, mins))
        self.dfs(turnedOn, hours+1, res)
