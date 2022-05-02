# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        n = 0
        while current:
            n+=1
            current = current.next
        middle = n // 2
        i = 0
        
        def reverse(head):
            ans = None
            while head:
                next_ = head.next
                head.next = ans
                ans = head
                head = next_
            return ans
        
        first = second = head
        while i < middle:
            second = second.next
            i += 1
        second = reverse(second)
        
        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True
