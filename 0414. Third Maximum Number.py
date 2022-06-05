class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_2 = sorted(nums)[::-1]
        nums_2 = list(dict.fromkeys(nums_2))
        if len(nums_2) >= 3:
            return(nums_2[2])
        else:
            return(nums_2[0])
