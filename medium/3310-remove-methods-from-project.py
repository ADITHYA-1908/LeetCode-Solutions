from typing import List


class Solution:
    def remainingMethods(
        self,
        n: int,
        k: int,
        invocations: List[List[int]]
    ) -> List[int]:

        graph = [[] for _ in range(n)]

        for source, destination in invocations:
            graph[source].append(destination)

        # Step 1: Find all suspicious methods reachable from k
        suspicious = [False] * n
        stack = [k]
        suspicious[k] = True

        while stack:
            method = stack.pop()

            for invoked_method in graph[method]:
                if not suspicious[invoked_method]:
                    suspicious[invoked_method] = True
                    stack.append(invoked_method)

        # Step 2: Check whether a non-suspicious method invokes
        # any suspicious method
        for source, destination in invocations:
            if not suspicious[source] and suspicious[destination]:
                # Suspicious methods cannot be removed
                return list(range(n))

        # Step 3: Return only non-suspicious methods
        return [
            method
            for method in range(n)
            if not suspicious[method]
        ]
