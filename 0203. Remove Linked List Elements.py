# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        # Method 1
        new_head = pre = ListNode(0)
        pre.next = head
        
        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
        
        return new_head.next
        
        # Method 2 快慢指針法
        new_head = ListNode(0)
        new_head.next = head
        fast, slow = head, new_head
        while fast:
            if fast.val != val:
                slow.next.val = fast.val
                slow = slow.next    
            fast = fast.next
        slow.next = None
        return new_head.next
