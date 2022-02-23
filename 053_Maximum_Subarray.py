class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_ = 0
        maxsum = -10000
        for i in range(len(nums)):
            if sum_ > 0:
                sum_ += nums[i]
            else:
                sum_ = nums[i]
            if sum_ > maxsum:
                maxsum = sum_
        return maxsum
