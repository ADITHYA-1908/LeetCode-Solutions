class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        ans = []

        def build_remaining():
            result = []
            for i in range(26):
                result.append(chr(ord('a') + i) * freq[i])
            return ''.join(result)

        for i in range(n):
            t = ord(target[i]) - ord('a')

            # Try to keep this character equal to target
            if freq[t] > 0:
                ans.append(target[i])
                freq[t] -= 1
                continue

            # Cannot stay equal.
            # Try the smallest character greater than target[i].
            for c in range(t + 1, 26):
                if freq[c] > 0:
                    freq[c] -= 1
                    ans.append(chr(ord('a') + c))

                    return ''.join(ans) + build_remaining()

            # No greater character available.
            # Backtrack to an earlier position.
            break
        else:
            # We exactly formed target, but answer must be STRICTLY greater.
            i = n

        # Backtrack
        while ans:
            pos = len(ans) - 1

            old = ans.pop()
            freq[ord(old) - ord('a')] += 1

            current = ord(target[pos]) - ord('a')

            for c in range(current + 1, 26):
                if freq[c] > 0:
                    freq[c] -= 1
                    ans.append(chr(ord('a') + c))

                    return ''.join(ans) + build_remaining()

        return ""
