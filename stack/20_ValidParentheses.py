class Solution:
    # Time: O(n)
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for char in s:
            if char not in closeToOpen:
                stack.append(char)
            else:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
        
        return True if len(stack) == 0 else False