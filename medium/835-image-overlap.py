class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)

        ones1 = []
        ones2 = []

        # Store positions of all 1s
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    ones1.append((i, j))
                if img2[i][j] == 1:
                    ones2.append((i, j))

        shifts = {}
        ans = 0

        # Compare every 1 in img1 with every 1 in img2
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shift = (r2 - r1, c2 - c1)
                shifts[shift] = shifts.get(shift, 0) + 1
                ans = max(ans, shifts[shift])

        return ans
