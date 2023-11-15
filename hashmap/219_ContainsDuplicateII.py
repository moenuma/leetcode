class Solution:

    def containsNearbyDuplicate1(self, nums: List[int], k: int) -> bool:

        hashMap = {}
        for idx, num in enumerate(nums):
            if num in hashMap and abs(hashMap[num]-idx) <= k:
                    return True
            else:
                hashMap[num] = idx
        
        return False

    # Sliding window
    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])

        return False