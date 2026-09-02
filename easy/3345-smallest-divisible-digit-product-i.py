class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            product = 1
            number = n

            while number > 0:
                digit = number % 10
                product *= digit
                number //= 10

            if product % t == 0:
                return n

            n += 1