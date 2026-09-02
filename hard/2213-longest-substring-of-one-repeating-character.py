from typing import List


class Node:
    def __init__(self, length=0, left_char="", right_char="",
                 prefix=0, suffix=0, best=0):
        self.length = length
        self.left_char = left_char
        self.right_char = right_char
        self.prefix = prefix
        self.suffix = suffix
        self.best = best


class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: List[int]
    ) -> List[int]:

        n = len(s)
        chars = list(s)

        tree = [Node() for _ in range(4 * n)]

        def merge(left, right):
            if left.length == 0:
                return right

            if right.length == 0:
                return left

            node = Node()

            node.length = left.length + right.length
            node.left_char = left.left_char
            node.right_char = right.right_char

            node.prefix = left.prefix
            node.suffix = right.suffix

            # If both segments meet with the same character
            if left.right_char == right.left_char:

                combined = left.suffix + right.prefix

                # Longest repeating substring
                node.best = max(left.best, right.best, combined)

                # Entire left segment is same character
                if left.prefix == left.length:
                    node.prefix = left.length + right.prefix

                # Entire right segment is same character
                if right.suffix == right.length:
                    node.suffix = right.length + left.suffix

            else:
                node.best = max(left.best, right.best)

            return node

        def build(index, low, high):
            if low == high:
                tree[index] = Node(
                    length=1,
                    left_char=chars[low],
                    right_char=chars[low],
                    prefix=1,
                    suffix=1,
                    best=1
                )
                return

            mid = (low + high) // 2

            build(index * 2, low, mid)
            build(index * 2 + 1, mid + 1, high)

            tree[index] = merge(
                tree[index * 2],
                tree[index * 2 + 1]
            )

        def update(index, low, high, position, new_char):
            if low == high:
                chars[position] = new_char

                tree[index] = Node(
                    length=1,
                    left_char=new_char,
                    right_char=new_char,
                    prefix=1,
                    suffix=1,
                    best=1
                )
                return

            mid = (low + high) // 2

            if position <= mid:
                update(
                    index * 2,
                    low,
                    mid,
                    position,
                    new_char
                )
            else:
                update(
                    index * 2 + 1,
                    mid + 1,
                    high,
                    position,
                    new_char
                )

            tree[index] = merge(
                tree[index * 2],
                tree[index * 2 + 1]
            )

        build(1, 0, n - 1)

        answer = []

        for position, new_char in zip(queryIndices, queryCharacters):

            if chars[position] != new_char:
                update(
                    1,
                    0,
                    n - 1,
                    position,
                    new_char
                )

            answer.append(tree[1].best)

        return answer