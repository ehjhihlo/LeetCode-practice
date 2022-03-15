# 用龜兔賽跑算法來解，如果快的有追上慢的，代表有形成一個圈圈
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
