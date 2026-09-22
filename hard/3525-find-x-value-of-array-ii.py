class Solution(object):
    def resultArray(self, nums, k, queries):
        n = len(nums)

        # Each segment-tree node stores:
        # prod = product of the entire segment modulo k
        # cnt[r] = number of non-empty prefixes with product % k == r

        size = 1
        while size < n:
            size *= 2

        tree_prod = [1] * (2 * size)
        tree_cnt = [[0] * k for _ in range(2 * size)]

        # Build leaves
        for i in range(n):
            rem = nums[i] % k
            pos = size + i

            tree_prod[pos] = rem
            tree_cnt[pos][rem] = 1

        def merge(left_prod, left_cnt, right_prod, right_cnt):
            prod = (left_prod * right_prod) % k

            # Prefixes completely inside the left segment
            cnt = left_cnt[:]

            # Prefixes that contain all of the left segment
            # and then a prefix of the right segment
            for r in range(k):
                cnt[(left_prod * r) % k] += right_cnt[r]

            return prod, cnt

        # Build segment tree
        for i in range(size - 1, 0, -1):
            prod, cnt = merge(
                tree_prod[2 * i],
                tree_cnt[2 * i],
                tree_prod[2 * i + 1],
                tree_cnt[2 * i + 1]
            )

            tree_prod[i] = prod
            tree_cnt[i] = cnt

        # Point update
        def update(index, value):
            pos = size + index
            rem = value % k

            tree_prod[pos] = rem
            tree_cnt[pos] = [0] * k
            tree_cnt[pos][rem] = 1

            pos //= 2

            while pos:
                prod, cnt = merge(
                    tree_prod[2 * pos],
                    tree_cnt[2 * pos],
                    tree_prod[2 * pos + 1],
                    tree_cnt[2 * pos + 1]
                )

                tree_prod[pos] = prod
                tree_cnt[pos] = cnt

                pos //= 2

        # Query all non-empty prefixes of nums[start:]
        def query(start):
            l = size + start
            r = size + n

            left_prod = 1
            left_cnt = [0] * k

            right_prod = 1
            right_cnt = [0] * k

            while l < r:
                if l & 1:
                    left_prod, left_cnt = merge(
                        left_prod,
                        left_cnt,
                        tree_prod[l],
                        tree_cnt[l]
                    )
                    l += 1

                if r & 1:
                    r -= 1
                    right_prod, right_cnt = merge(
                        tree_prod[r],
                        tree_cnt[r],
                        right_prod,
                        right_cnt
                    )

                l //= 2
                r //= 2

            _, result_cnt = merge(
                left_prod,
                left_cnt,
                right_prod,
                right_cnt
            )

            return result_cnt

        result = []

        for index, value, start, x in queries:
            # The update persists for all subsequent queries
            update(index, value)

            # Every possible remaining array is a non-empty prefix
            # of nums[start:]
            counts = query(start)

            result.append(counts[x])

        return result
