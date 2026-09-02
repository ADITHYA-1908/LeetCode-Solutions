from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0

        for num in nums:
            xor ^= num

        # Entire array already has non-zero XOR
        if xor != 0:
            return len(nums)

        # Entire XOR is 0
        # Remove any non-zero element
        for num in nums:
            if num != 0:
                return len(nums) - 1

        # All elements are 0
        return 0
