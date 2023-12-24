class Solution:
    # Time: O(n^2*m)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sizeS = len(s)
        dp = [False] * (sizeS + 1)
        dp[sizeS] = True

        for i in range(sizeS-1, -1, -1):
            for w in wordDict:
                if (i+len(w) <= sizeS) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        
        return dp[0]

