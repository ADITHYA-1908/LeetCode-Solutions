from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]

        # Find sum of longest sequential prefix
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # Store all numbers for fast lookup
        values = set(nums)

        # Find smallest missing integer >= total
        while total in values:
            total += 1

        return total