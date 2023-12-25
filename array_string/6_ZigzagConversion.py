class Solution:
    # Time: O(n) (length of string)
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        increment = 2 * (numRows - 1)
        res = ""

        for row in range(numRows):
            for i in range(row, len(s), increment):
                res += s[i]
                if (row > 0 and row < numRows - 1 and
                    i + increment - 2*row < len(s)):
                    res += s[i + increment - 2*row]

        return res

