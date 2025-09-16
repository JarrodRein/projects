# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def get_kth(curr: ListNode, k: int) -> ListNode | None:
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr
        
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = get_kth(groupPrev, k)
            if npt kth:
                break
            groupNext = kth.next
            # reverse group
            prev, curr = kth.next, group_prev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next