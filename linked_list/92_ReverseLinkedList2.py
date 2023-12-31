# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time: O(n)
    # Space: O(n)
    def reverseBetween1(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        index = 1
        current = head
        reverseMap = {}

        while current:
            if index >= left and index <= right:
                reverseMap[right+left-index] = current.val
            current = current.next
            index += 1
        
        index = 1
        current = head
        res = ListNode()
        resPtr = res

        while current:
            if index >= left and index <= right:
                resPtr.next = ListNode(reverseMap[index])
            else:
                resPtr.next = ListNode(current.val)
            current = current.next
            resPtr = resPtr.next
            index += 1
        
        return res.next
    
    # Time: O(n)
    # Space: O(1)
    def reverseBetween2(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        leftPrev, cur = dummy, head
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next
        
        prev = None
        for i in range(right - left + 1):
            tempNext = cur.next
            cur.next = prev
            prev, cur = cur, tempNext
        
        leftPrev.next.next = cur
        leftPrev.next = prev

        return dummy.next