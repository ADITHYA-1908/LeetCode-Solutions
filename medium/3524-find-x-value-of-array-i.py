class Solution(object):
    def resultArray(self, nums, k):
        ans = [0] * k

        # dp[r] = number of subarrays ending at the previous index
        # whose product % k == r
        dp = [0] * k

        for num in nums:
            rem = num % k
            new_dp = [0] * k

            # Start a new subarray with the current element
            new_dp[rem] += 1

            # Extend all previous subarrays
            for r in range(k):
                if dp[r]:
                    new_rem = (r * rem) % k
                    new_dp[new_rem] += dp[r]

            # Add counts of current subarrays to the answer
            for r in range(k):
                ans[r] += new_dp[r]

            dp = new_dp

        return ans
