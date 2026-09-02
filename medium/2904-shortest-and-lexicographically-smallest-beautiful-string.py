class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ans = ""
        min_len = float('inf')

        left = 0
        ones = 0

        for right in range(n):
            if s[right] == '1':
                ones += 1

            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            while ones == k and left <= right:
                curr = s[left:right + 1]

                if len(curr) < min_len:
                    min_len = len(curr)
                    ans = curr
                elif len(curr) == min_len and curr < ans:
                    ans = curr

                if s[left] == '1':
                    ones -= 1
                left += 1

        return ans
