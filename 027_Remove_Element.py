class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums) - 1
        while(start<=end):
            if nums[start] != val:
                start+=1
            else:
                nums[start], nums[end] = nums[end], nums[start]
                end-=1
        return start
