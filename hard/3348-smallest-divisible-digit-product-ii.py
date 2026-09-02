class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Prime factor contribution of each digit:
        # digit -> (power of 2, power of 3, power of 5, power of 7)
        fac = [
            (0, 0, 0, 0),  # 0 - not allowed
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0),  # 9
        ]

        # ---------------------------------------------------------
        # Step 1: Factorize t using only 2, 3, 5, 7
        # ---------------------------------------------------------
        need = [0, 0, 0, 0]

        for i, p in enumerate((2, 3, 5, 7)):
            while t % p == 0:
                t //= p
                need[i] += 1

        # No digit 1..9 contains any other prime factor.
        if t != 1:
            return "-1"

        # ---------------------------------------------------------
        # Minimum number of digits required to provide
        # a powers of 2, b powers of 3, c powers of 5,
        # d powers of 7.
        # ---------------------------------------------------------
        def min_digits(a, b, c, d):
            if a < 0:
                a = 0
            if b < 0:
                b = 0
            if c < 0:
                c = 0
            if d < 0:
                d = 0

            # 5 and 7 need one digit each.
            ans = 10**9

            # x = number of digit 6's used.
            #
            # We only need to check x = 0..5.
            # Increasing x by 6 can never improve the answer.
            limit = min(a, b, 5)

            for x in range(limit + 1):
                aa = a - x
                bb = b - x

                # powers of 2 can be packed using digit 8
                cnt2 = (aa + 2) // 3

                # powers of 3 can be packed using digit 9
                cnt3 = (bb + 1) // 2

                ans = min(ans, x + cnt2 + cnt3)

            return ans + c + d

        # ---------------------------------------------------------
        # Construct lexicographically smallest suffix of `length`
        # digits that satisfies remaining requirements.
        # ---------------------------------------------------------
        def build_suffix(req, length):
            a, b, c, d = req

            required = min_digits(a, b, c, d)

            if required > length:
                return None

            result = []

            # Extra positions should obviously be 1's because
            # 1 is the smallest zero-free digit.
            extra = length - required

            if extra:
                result.append("1" * extra)
                length -= extra

            # Only a small number of positions remain here.
            while length:
                for digit in range(1, 10):
                    x2, x3, x5, x7 = fac[digit]

                    na = max(0, a - x2)
                    nb = max(0, b - x3)
                    nc = max(0, c - x5)
                    nd = max(0, d - x7)

                    if min_digits(na, nb, nc, nd) <= length - 1:
                        result.append(str(digit))

                        a, b, c, d = na, nb, nc, nd
                        length -= 1
                        break

            return "".join(result)

        n = len(num)

        # ---------------------------------------------------------
        # Calculate total factors contained in num.
        # ---------------------------------------------------------
        prefix = [0, 0, 0, 0]
        first_zero = n

        for i, ch in enumerate(num):
            digit = ord(ch) - 48

            if digit == 0 and first_zero == n:
                first_zero = i

            if digit != 0:
                f = fac[digit]
                prefix[0] += f[0]
                prefix[1] += f[1]
                prefix[2] += f[2]
                prefix[3] += f[3]

        # ---------------------------------------------------------
        # Is num itself already valid?
        # ---------------------------------------------------------
        if first_zero == n:
            if (
                prefix[0] >= need[0]
                and prefix[1] >= need[1]
                and prefix[2] >= need[2]
                and prefix[3] >= need[3]
            ):
                return num

        # ---------------------------------------------------------
        # Try changing the rightmost possible digit.
        #
        # Rightmost change gives the smallest possible number.
        # ---------------------------------------------------------
        pref = prefix[:]

        for i in range(n - 1, -1, -1):
            current = ord(num[i]) - 48

            # Remove current digit.
            if current != 0:
                f = fac[current]
                pref[0] -= f[0]
                pref[1] -= f[1]
                pref[2] -= f[2]
                pref[3] -= f[3]

            # If there is already a zero before this position,
            # keeping that prefix is impossible.
            if i > first_zero:
                continue

            suffix_length = n - i - 1

            # Increase current digit.
            start = max(1, current + 1)

            for digit in range(start, 10):
                f = fac[digit]

                req = (
                    max(0, need[0] - pref[0] - f[0]),
                    max(0, need[1] - pref[1] - f[1]),
                    max(0, need[2] - pref[2] - f[2]),
                    max(0, need[3] - pref[3] - f[3]),
                )

                if min_digits(*req) <= suffix_length:
                    suffix = build_suffix(req, suffix_length)

                    return num[:i] + str(digit) + suffix

        # ---------------------------------------------------------
        # No answer having the same number of digits.
        #
        # Build the smallest number with more digits.
        # ---------------------------------------------------------
        required_length = min_digits(*need)

        length = max(n + 1, required_length)

        return build_suffix(tuple(need), length)