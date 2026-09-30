# LeetCode 1111: Maximum Nesting Depth of Two Valid Parentheses Strings
# Difficulty: Medium
# Approach: Greedy / nesting depth parity
# Time Complexity: O(n)
# Space Complexity: O(n) for the output

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        answer = []
        depth = 0

        for ch in seq:
            if ch == '(':
                depth += 1
                answer.append(depth % 2)
            else:
                answer.append(depth % 2)
                depth -= 1

        return answer
