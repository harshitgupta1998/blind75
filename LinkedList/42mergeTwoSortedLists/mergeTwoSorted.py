# merge two sorted lists (leetcode 21)
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        l, r = head, head
        while r and r.next:
            l = l.next
            r = r.next.next
            if l == r:
                return True
        return False
