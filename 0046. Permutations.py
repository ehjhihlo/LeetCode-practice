class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        p_list = list(permutations(nums))
        p_list = [list(i) for i in p_list]
        return p_list
