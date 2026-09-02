from typing import List
from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            n = len(coins)
            total = 0

            for mask in range(1, 1 << n):
                current_lcm = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        current_lcm = lcm(current_lcm, coins[i])
                        bits += 1

                        if current_lcm > x:
                            break

                if current_lcm <= x:
                    if bits % 2 == 1:
                        total += x // current_lcm
                    else:
                        total -= x // current_lcm

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left
