class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = sorted(nums1 + nums2)
        if len(merge) % 2 == 0:
            return (merge[int(len(merge)/2-1)] + merge[int(len(merge)/2)])/2
        elif len(merge) % 2 != 0:
            return merge[int(len(merge)//2)]
