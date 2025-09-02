# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return None
        if k == 1:
            return lists[0] # Only one list, return it as is.
        if k == 2:
            return self.mergeTwoLists(lists[0], lists[1])   # Use the helper function to merge two lists.   
        
        mid = k // 2
        left_merged = self.mergeKLists(lists[:mid])  # Recursively merge the left half.
        right_merged = self.mergeKLists(lists[mid:]) # Recursively merge the right half.  
        return self.mergeTwoLists(left_merged, right_merged)
    