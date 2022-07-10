# Dynamic programming + max sliding window
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if nums == None:
            return 0
        dp = [float(-inf)]*len(nums)
        dp[0] = nums[0]
        dq = collections.deque()
        dq.append(0)
        
        for i in range(1, len(nums)):
            # for j in range(max(i-k,0),i):
            #     dp[i] = max(dp[i], nums[i]+dp[j])
            while dq and dq[0] < i-k:
                dq.popleft()
            dp[i] = nums[i] + dp[dq[0]]
            while dq and dp[dq[-1]]<=dp[i]:
                dq.pop()
            dq.append(i)
        return dp[-1]
