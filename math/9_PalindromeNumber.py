class Solution:
    # Convert int to str
    # Time: O(n)
    # Space: O(1)
    def isPalindrome1(self, x: int) -> bool:
        s = str(x)
        r = len(s) - 1

        for l in range(len(s)):
            if s[l] != s[r]:
                return False
            r -= 1
            
        return True
    
    def isPalindrome2(self, x: int) -> bool:
        pass