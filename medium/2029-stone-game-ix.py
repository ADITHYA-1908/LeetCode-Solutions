from typing import List

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0, 0, 0]

        for x in stones:
            cnt[x % 3] += 1

        # If the number of remainder-0 stones is even,
        # Alice needs at least one remainder-1 and one remainder-2 stone.
        if cnt[0] % 2 == 0:
            return cnt[1] > 0 and cnt[2] > 0

        # If remainder-0 count is odd,
        # the difference between remainder-1 and remainder-2
        # must be greater than 2.
        return abs(cnt[1] - cnt[2]) > 2
