class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        dict_ = {value:i for i, value in enumerate(nums2)}
        for i in nums1:
            index = dict_[i]+1
            while index< len(nums2) and i >= nums2[index]:
                index+=1
            if index == len(nums2):
                res.append(-1)
            else:
                res.append(nums2[index])
        return res
