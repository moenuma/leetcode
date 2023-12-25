class Solution:
    # Time: O(m*n)
    # Space: O(1)
    def strStr1(self, haystack: str, needle: str) -> int:
        n_size = len(needle)

        for i in range(len(haystack)):
            if i + n_size <= len(haystack):
                word = haystack[i:i+n_size]
                if word == needle:
                    return i
            else:
                return -1

        return -1
    
    #TODO Use KMP
    def strStr2(self, haystack: str, needle: str) -> int:
        return