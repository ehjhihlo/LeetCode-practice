class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0 
        if min(coins) > amount:
            return -1
        
        list_ = [-1 for i in range(0,amount+1)]
        for i in coins:
            if i > len(list_)-1:
                continue
            list_[i] = 1
            for j in range(i+1, amount+1):
                if list_[j-i]==-1:
                    continue
                elif list_[j]==-1:
                    list_[j] = list_[j-i]+1
                else:
                    list_[j] = min(list_[j], list_[j-i]+1)
        
        return list_[amount]
