# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time: O(n)
    # Space: O(n)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        ptr = res
        carry = 0
        while l1 or l2 or carry:
            twoSum = carry
            if l1:
                twoSum += l1.val
                l1 = l1.next
            if l2:
                twoSum += l2.val
                l2 = l2.next
            carry = twoSum // 10
            ptr.next = ListNode(twoSum % 10)
            ptr = ptr.next
        
        return res.next