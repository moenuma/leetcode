"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    # Time: O(n)
    # Space: O(n)
    def connect1(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None

        queue = deque()
        queue.append(root)

        while queue:
            cur = None
            nxt = None

            for _ in range(len(queue)):
                if not cur:
                    cur = queue.popleft()
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                elif not nxt:
                    nxt = queue.popleft()
                    cur.next = nxt
                    if nxt.left:
                        queue.append(nxt.left)
                    if nxt.right:
                        queue.append(nxt.right)
                else:
                    cur = queue.popleft()
                    nxt.next = cur
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                    nxt = cur
        
        return root

    # BFS
    # Time: O(n)
    # Space: O(1)
    def connect2(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None

        head = root # head points to the leftmost node
        dummy = Node(0) 

        # iterate each level
        while head:
            cur = head
            prev = dummy # prev points to the leftmost node one level below head

            # iterate all the nodes on the level
            while cur:
                if cur.left:
                    prev.next = cur.left
                    prev = prev.next
                if cur.right:
                    prev.next = cur.right
                    prev = prev.next
                cur = cur.next
            
            head = dummy.next
            dummy.next = None # reset dummy node
        
        return root
