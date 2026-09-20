class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = float('inf')

        # best[i] = minimum length of a valid subarray
        # completely inside arr[0:i]
        best = [INF] * (n + 1)

        left = 0
        curr_sum = 0
        ans = INF
        current_best = INF

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                # best[left] contains a subarray
                # before the current one
                if best[left] != INF:
                    ans = min(ans, length + best[left])

                current_best = min(current_best, length)

            best[right + 1] = current_best

        return -1 if ans == INF else ans
