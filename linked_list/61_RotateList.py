# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time: O(n)
    # Space: O(1)
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head

        tail = head
        length = 1
        while tail.next:
            length += 1
            tail = tail.next

        k %= length
        if k == 0: return head

        cur = head
        i = 0
        while i < (length - k - 1):
            cur = cur.next
            i += 1

        newHead = cur.next
        cur.next = None
        tail.next = head
        
        return newHead