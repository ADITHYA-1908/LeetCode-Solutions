from functools import lru_cache

class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Path length must be even
        if (m + n - 1) % 2 != 0:
            return False

        @lru_cache(None)
        def dfs(r, c, balance):

            # Invalid if ')' exceeds '('
            if balance < 0:
                return False

            # Number of cells remaining after current cell
            remaining = (m - r - 1) + (n - c - 1)

            # We need at least 'balance' closing brackets
            if balance > remaining:
                return False

            # Bottom-right cell
            if r == m - 1 and c == n - 1:
                return balance == 0

            # Move down
            if r + 1 < m:
                change = 1 if grid[r + 1][c] == '(' else -1

                if dfs(r + 1, c, balance + change):
                    return True

            # Move right
            if c + 1 < n:
                change = 1 if grid[r][c + 1] == '(' else -1

                if dfs(r, c + 1, balance + change):
                    return True

            return False

        # Start cell
        start = 1 if grid[0][0] == '(' else -1

        return dfs(0, 0, start)
