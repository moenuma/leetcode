class Solution:
    def rob1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        # base case
        dp[n-1], dp[n-2] = nums[n-1], max(nums[n-2], nums[n-1])

        for i in range(n-3, -1, -1):
            dp[i] = max((nums[i]+dp[i+2]), dp[i+1])
        
        return dp[0]

    # time: O(n)
    # space: O(1)
    def rob2(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2