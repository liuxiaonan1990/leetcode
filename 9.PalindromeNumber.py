class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        self.s_list = list(s)

        i = 0
        j = len(self.s_list) - 1
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