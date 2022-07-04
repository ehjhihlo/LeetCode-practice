# Use Greedy Alogorithm
class Solution:
    def candy(self, ratings: List[int]) -> int:
        list_ = [1]*len(ratings)
        for i in range(len(ratings)-1):
            if ratings[i] < ratings[i+1]:
                list_[i+1] = list_[i] + 1
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i] < ratings[i-1] and list_[i] >= list_[i-1]:
                list_[i-1] = list_[i] + 1
        return sum(list_)
