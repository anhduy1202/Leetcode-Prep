
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        slow = head
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            if slow == fast:
                return True
            else:
                slow = slow.next
        return False