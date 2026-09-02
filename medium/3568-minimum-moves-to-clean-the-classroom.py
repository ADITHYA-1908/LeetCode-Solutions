from collections import deque
from typing import List


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        litter_id = {}
        start = None
        idx = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = idx
                    idx += 1

        total_litter = idx
        full_mask = (1 << total_litter) - 1

        # State: row, col, collected_mask, remaining_energy
        queue = deque([(start[0], start[1], 0, energy, 0)])

        # For each (r, c, mask), remember the maximum energy
        # we've had when reaching that state.
        best_energy = {}

        best_energy[(start[0], start[1], 0)] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, mask, curr_energy, moves = queue.popleft()

            if mask == full_mask:
                return moves

            # Cannot move if energy is zero unless currently on R
            if curr_energy == 0 and classroom[r][c] != 'R':
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                if curr_energy == 0:
                    continue

                new_energy = curr_energy - 1
                new_mask = mask

                # Collect litter
                if classroom[nr][nc] == 'L':
                    bit = litter_id[(nr, nc)]
                    new_mask |= (1 << bit)

                # Reset energy
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                state = (nr, nc, new_mask)

                if best_energy.get(state, -1) >= new_energy:
                    continue

                best_energy[state] = new_energy
                queue.append((nr, nc, new_mask, new_energy, moves + 1))

        return -1
