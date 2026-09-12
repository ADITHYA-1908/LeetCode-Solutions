from bisect import bisect_right


class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # Add original index
        arr = [
            [l, r, w, i]
            for i, (l, r, w) in enumerate(intervals)
        ]

        # Sort by starting point
        arr.sort()
        starts = [x[0] for x in arr]

        # Find the first interval whose start > current end
        nxt = [0] * n
        for i in range(n):
            nxt[i] = bisect_right(starts, arr[i][1])

        # dp[i][k] = best (score, indices) using intervals from i onward,
        # choosing at most k intervals.
        dp = [[None] * 5 for _ in range(n + 1)]

        # Base cases
        for i in range(n + 1):
            dp[i][0] = (0, [])

        for k in range(1, 5):
            dp[n][k] = (0, [])

        # Fill DP from right to left
        for i in range(n - 1, -1, -1):
            for k in range(1, 5):
                # Option 1: skip current interval
                skip_score, skip_indices = dp[i + 1][k]

                # Option 2: take current interval
                next_score, next_indices = dp[nxt[i]][k - 1]
                take_score = arr[i][2] + next_score
                take_indices = [arr[i][3]] + next_indices

                # Choose the better option.
                if take_score > skip_score:
                    dp[i][k] = (take_score, take_indices)
                elif take_score < skip_score:
                    dp[i][k] = (skip_score, skip_indices)
                else:
                    # Same score -> lexicographically smaller indices
                    a = sorted(take_indices)
                    b = sorted(skip_indices)
                    if a < b:
                        dp[i][k] = (take_score, take_indices)
                    else:
                        dp[i][k] = (skip_score, skip_indices)

        return sorted(dp[0][4][1])
