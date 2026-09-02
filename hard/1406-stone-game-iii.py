from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        # dp[i] = maximum score difference the current player
        # can achieve from stoneValue[i:]
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            current_sum = 0
            dp[i] = float("-inf")

            # Take 1, 2, or 3 stones
            for take in range(1, 4):
                if i + take > n:
                    break

                current_sum += stoneValue[i + take - 1]

                # Opponent gets dp[i + take], so subtract it
                dp[i] = max(dp[i], current_sum - dp[i + take])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"