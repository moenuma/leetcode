class Solution:

    # O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}

        for idx, num in enumerate(nums):
            if target-num in hashMap:
                return [hashMap[target-num], idx]
            else:
                hashMap[num] = idx
