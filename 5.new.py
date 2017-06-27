class Solution(object):
    def checkPalindrome(self, start, end):
        if end - start == 0:
            return True
        if end - start == 1:
            if self.s_list[start] == self.s_list[end]:
                return True
            else:
                return False

        if end - start > 1:
            if self.s_list[start] == self.s_list[end]:
                return self.checkPalindrome(start + 1, end - 1)
            else:
                return False

    def check(self, start, end):

        i = start
        j = end
        while j - i > 1:
            if self.s_list[i] == self.s_list[j]:
                i += 1
                j -= 1
            else:
                return False

        if i == j:
            return True

        if i + 1 == j:
            if self.s_list[i] == self.s_list[j]:
                return True
            else:
                return False

    def check2(self, start, end):

        if (start + end) % 2 == 1:
            i = (start + end) / 2
            j = i + 1
        else:
            i = (start + end) / 2 - 1
            j = (start + end) / 2 + 1

        while i >= start:
            if self.s_list[i] != self.s_list[j]:
                return False
            else:
                i -= 1
                j += 1

        return True

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max = 1
        index = 0
        high = 0
        self.s_list = list(s)

        if len(self.s_list) < 2:
            return s

        for i in range(len(self.s_list)):
            #  print i, max
            for j in range(len(self.s_list) - 1, i, -1):
                #      print i, j, max
                if j < high:
                    continue

                if self.check(i, j):
                    if max < j - i + 1:
                        max = j - i + 1
                        index = i
                        high = j
                        print max, i, j

                    break
                else:
                    if max > j - i + 1:
                        break

        return s[index:index + max]

