class Solution:
    # time: O(n*m)
    def coinChange(self, coins: LIst[int], amount: int) -> int:
        dp = [-1] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if (i - coin) >= 0 and dp[i-coin] != -1:
                    current = dp[i-coin] + 1
                    # update first entry or min
                    if dp[i] == -1 or dp[i] > current:
                        dp[i] = current
        
        return dp[amount+1]
