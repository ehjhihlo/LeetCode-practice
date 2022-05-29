class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_ = {}
        if len(nums1)<len(nums2):
            nums1, nums2 = nums2, nums1
        for i in nums1:
            if i not in dict_:
                dict_[i] = 1
            else:
                dict_[i] += 1
        
        res = []
        for i in nums2:
            if i in dict_ and dict_[i]:
                dict_[i]-=1
                res.append(i)
        res = set(res)
        return res
