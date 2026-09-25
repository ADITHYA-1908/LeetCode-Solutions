"""LeetCode 1096 - Brace Expansion II (Hard).

Recursive descent parser using sets for union and Cartesian-product concatenation.
https://leetcode.com/problems/brace-expansion-ii/
"""

class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        i = 0
        n = len(expression)

        def parse():
            nonlocal i
            result = set()
            current = {""}

            while i < n and expression[i] != "}":
                if expression[i] == ",":
                    result |= current
                    current = {""}
                    i += 1
                elif expression[i] == "{":
                    i += 1
                    next_set = parse()
                    current = {a + b for a in current for b in next_set}
                else:
                    char = expression[i]
                    current = {word + char for word in current}
                    i += 1

            result |= current
            if i < n and expression[i] == "}":
                i += 1
            return result

        return sorted(parse())
