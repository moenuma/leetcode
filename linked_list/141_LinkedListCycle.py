# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Time: O(n)
    # Space: O(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        current = head

        while current:
            if current in seen:
                return True
            seen.add(current)
            current = current.next
        
        return False

    # Floyd's Tortoise and Hare
    # Time: O(n)
    # Space: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False