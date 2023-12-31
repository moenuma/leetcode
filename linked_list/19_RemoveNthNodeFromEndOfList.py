# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Use hash map
    # Time: O(n)
    # Space: O(n)
    def removeNthFromEnd1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        headMap = {}
        current = head
        index = 0

        while current:
            headMap[index] = current
            index += 1
            current = current.next

        # remove index - n
        if index-n-1 >= 0:
            headMap[index-n-1].next = headMap[index-n].next
        else:
            dummy.next = head.next

        return dummy.next

    # Use two pointers
    def removeNthFromEnd1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next

