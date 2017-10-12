class Solution(object):
    def func(self, n):
        if n == 1:
            result = "1"
            return result

        if n > 1:
            s = self.func(n - 1)

            result = ""
            count = 0
            char = s[0]
            for i in range(len(s)):
                if s[i] == char:
                    count += 1
                else:
                    result += str(count)
                    result += char

                    char = s[i]
                    count = 1

            result += str(count)
            result += char

            return result


    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        return self.func(n)