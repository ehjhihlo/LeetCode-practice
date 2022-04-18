class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictionary = dict()
        for i, n in enumerate(nums):
            if n in dictionary:
                if i - dictionary[n] <= k:
                    return True
            dictionary[n] = i
        return False
