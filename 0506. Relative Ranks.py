class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = sorted(score)[::-1]
        dict_ = {}
        for i in range(len(score)):
            if i+1 == 1:
                dict_[rank[i]] = "Gold Medal"
            elif i+1 == 2:
                dict_[rank[i]] = "Silver Medal"
            elif i+1 == 3:
                dict_[rank[i]] = "Bronze Medal"
            else:
                dict_[rank[i]] = str(i+1)
        return [dict_[i] for i in score]
