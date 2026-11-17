# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # save current head
        prev = None
        curr = head
        while curr:    
            # save next
            nxt = curr.next
            # reverse the link
            curr.next = prev
            # move prev to the current
            prev = curr
            # move current to the next
            curr = nxt
        return prev
