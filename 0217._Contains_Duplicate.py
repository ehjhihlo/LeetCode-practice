class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        prelen = len(nums)
        postlen = len(set(nums))
        if prelen == postlen:
            return False
        else:
            return True
