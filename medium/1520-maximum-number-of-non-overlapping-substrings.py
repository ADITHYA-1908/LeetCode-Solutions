class Solution:
    def maxNumOfSubstrings(self, s: str):
        n = len(s)

        # Find first and last occurrence of every character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            x = ord(ch) - ord('a')
            first[x] = min(first[x], i)
            last[x] = i

        intervals = []

        # Try to create a valid substring starting from
        # the first occurrence of each character
        for i in range(n):
            x = ord(s[i]) - ord('a')

            # Only start from the first occurrence
            if i != first[x]:
                continue

            l = i
            r = last[x]
            valid = True

            j = l
            while j <= r:
                y = ord(s[j]) - ord('a')

                # This character appeared before l,
                # so this substring cannot be valid
                if first[y] < l:
                    valid = False
                    break

                # Extend the substring if needed
                r = max(r, last[y])
                j += 1

            if valid:
                intervals.append((l, r))

        # Choose intervals with the earliest ending position
        intervals.sort(key=lambda x: x[1])

        result = []
        end = -1

        for l, r in intervals:
            if l > end:
                result.append(s[l:r + 1])
                end = r

        return result