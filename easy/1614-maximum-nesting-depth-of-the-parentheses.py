"""LeetCode 1614: Maximum Nesting Depth of the Parentheses.
Time: O(n) | Space: O(1)
"""

class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth = 0

        for ch in s:
            if ch == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif ch == ')':
                depth -= 1

        return max_depth
