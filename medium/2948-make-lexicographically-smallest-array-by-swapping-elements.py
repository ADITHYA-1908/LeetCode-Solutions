from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        pairs = sorted((value, index) for index, value in enumerate(nums))
        ans = nums[:]

        start = 0

        while start < n:
            end = start

            while end + 1 < n and pairs[end + 1][0] - pairs[end][0] <= limit:
                end += 1

            indices = sorted(pairs[i][1] for i in range(start, end + 1))
            values = [pairs[i][0] for i in range(start, end + 1)]

            for index, value in zip(indices, values):
                ans[index] = value

            start = end + 1

        return ans
