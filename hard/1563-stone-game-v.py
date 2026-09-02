from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]

        # bestLeft[i][j] =
        # max(dp[i][k] + sum(i..k)) for valid k in [i..j]
        bestLeft = [[0] * n for _ in range(n)]

        # bestRight[i][j] =
        # max(dp[k][j] + sum(k..j)) for valid k in [i..j]
        bestRight = [[0] * n for _ in range(n)]

        for i in range(n):
            bestLeft[i][i] = stoneValue[i]
            bestRight[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                total = prefix[j + 1] - prefix[i]

                # Find largest k such that:
                # sum(i..k) <= sum(k+1..j)
                lo, hi = i, j - 1
                split = i - 1

                while lo <= hi:
                    mid = (lo + hi) // 2

                    left = prefix[mid + 1] - prefix[i]

                    if left * 2 <= total:
                        split = mid
                        lo = mid + 1
                    else:
                        hi = mid - 1

                ans = 0

                # Cases where left <= right
                if split >= i:
                    ans = max(ans, bestLeft[i][split])

                # Cases where right <= left
                start = split + 1

                if start <= j - 1:
                    ans = max(ans, bestRight[start + 1][j])

                # Equality case needs special handling
                if split >= i:
                    left_sum = prefix[split + 1] - prefix[i]
                    right_sum = total - left_sum

                    if left_sum == right_sum:
                        ans = max(
                            ans,
                            left_sum + dp[split + 1][j]
                        )

                dp[i][j] = ans

                whole_sum = total + dp[i][j]

                bestLeft[i][j] = max(
                    bestLeft[i][j - 1],
                    whole_sum
                )

                bestRight[i][j] = max(
                    bestRight[i + 1][j],
                    whole_sum
                )

        return dp[0][n - 1]
