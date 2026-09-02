from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = Counter(s)

        odd = [c for c in freq if freq[c] % 2]

        if len(odd) > 1:
            return ""

        mid = odd[0] if odd else ""
        m = n // 2

        cnt = [0] * 26
        for c in freq:
            cnt[ord(c) - ord('a')] = freq[c] // 2

        t = target[:m]

        remaining = cnt[:]
        prefix = []
        i = 0

        # Match target's first half as much as possible
        while i < m:
            x = ord(t[i]) - ord('a')

            if remaining[x] == 0:
                break

            remaining[x] -= 1
            prefix.append(t[i])
            i += 1

        while True:
            if i < m:
                x = ord(t[i]) - ord('a')

                # Pick the smallest character greater than target[i]
                for c in range(x + 1, 26):
                    if remaining[c] > 0:
                        remaining[c] -= 1

                        left = prefix + [chr(c + ord('a'))]

                        # Fill remaining positions lexicographically smallest
                        for k in range(26):
                            left.extend(
                                [chr(k + ord('a'))] * remaining[k]
                            )

                        left = "".join(left)
                        palindrome = left + mid + left[::-1]

                        if palindrome > target:
                            return palindrome

                        remaining[c] += 1

            # If whole first half matched target
            if i == m:
                left = "".join(prefix)
                palindrome = left + mid + left[::-1]

                if palindrome > target:
                    return palindrome

            # Backtrack
            if i == 0:
                return ""

            i -= 1

            restored = ord(prefix.pop()) - ord('a')
            remaining[restored] += 1
