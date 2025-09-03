# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = head
        if not n or not n.next:
            return head
        newHead = head.next
        prev = None
        while n and n.next:
            first = n
            second = n.next
            nxt = n.next.next
            
            if prev:
                prev.next = second
            second.next = first
            first.next = nxt
            
            prev = first
            n = nxt

        return newHead