class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        rows = {}

        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            rows[row].add(seat)

        # Rows with no reservations can fit 2 families
        answer = (n - len(rows)) * 2

        for seats in rows.values():
            left = all(seat not in seats for seat in [2, 3, 4, 5])
            middle = all(seat not in seats for seat in [4, 5, 6, 7])
            right = all(seat not in seats for seat in [6, 7, 8, 9])

            # Left and right don't overlap, so both can be used
            if left and right:
                answer += 2

            # Otherwise at most one block can be used
            elif left or middle or right:
                answer += 1

        return answer
