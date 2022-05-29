class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left<=right:
            mid = (left+right)//2
            val = mid*mid
            if val == num:
                return True
            elif val < num:
                left = mid+1
            elif val > num:
                right = mid-1
        return False
