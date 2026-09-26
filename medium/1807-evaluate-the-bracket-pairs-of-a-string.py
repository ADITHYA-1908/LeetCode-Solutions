# LeetCode 1807: Evaluate the Bracket Pairs of a String
# Difficulty: Medium
# Approach: Hash map and string traversal
# Time: O(n + k) average; Space: O(n + k)

from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        mp = dict(knowledge)
        result = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                j = s.find(')', i)
                key = s[i + 1:j]
                result.append(mp.get(key, '?'))
                i = j + 1
            else:
                result.append(s[i])
                i += 1

        return ''.join(result)
