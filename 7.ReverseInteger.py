class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = 0
        max = 2 ** 31 - 1
        min = -2 ** 31
        print max, min
        if x > max or x < min:
            return 0

        if x >= 0:
            a = x / 10
            b = x % 10
            while a > 0:
                y = y * 10 + b

                b = a % 10
                a = a / 10

            y = y * 10 + b

            if y > max or y < min:
                return 0

            return y

        else:
            x = 0 - x

            a = x / 10
            b = x % 10
            while a > 0:
                y = y * 10 + b

                b = a % 10
                a = a / 10

            y = y * 10 + b

            if y > max or y < min:
                return 0

            return 0 - y




