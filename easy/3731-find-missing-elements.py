from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        present = set(nums)
        minimum = min(nums)
        maximum = max(nums)

        missing = []

        for number in range(minimum, maximum + 1):
            if number not in present:
                missing.append(number)

        return missing