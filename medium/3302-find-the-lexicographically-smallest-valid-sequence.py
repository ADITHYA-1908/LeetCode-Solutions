from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        # suffix[j] = latest index in word1 that can be used
        # as the starting point to match word2[j:]
        suffix = [-1] * m

        i = n - 1
        for j in range(m - 1, -1, -1):
            while i >= 0 and word1[i] != word2[j]:
                i -= 1

            if i < 0:
                break

            suffix[j] = i
            i -= 1

        ans = []
        pos = 0
        changed = False

        for j in range(m):
            while pos < n:
                # Case 1: characters already match
                if word1[pos] == word2[j]:
                    ans.append(pos)
                    pos += 1
                    break

                # Case 2: use our one allowed mismatch
                if not changed:
                    # If this is the last character, mismatch is always okay.
                    if j == m - 1:
                        ans.append(pos)
                        pos += 1
                        changed = True
                        break

                    # Remaining word2[j+1:] must still be matchable
                    if suffix[j + 1] != -1 and pos < suffix[j + 1]:
                        ans.append(pos)
                        pos += 1
                        changed = True
                        break

                pos += 1
            else:
                return []

        return ans