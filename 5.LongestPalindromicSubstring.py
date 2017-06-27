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

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max = 1
        index = 0
        self.s_list = list(s)
        i = 0
        s_dict = {}
        while i < len(self.s_list):
            c = self.s_list[i]
            if s_dict.has_key(c):
                s_dict[c].append(i)
            else:
                v = []
                v.append(i)
                s_dict[c] = v

            i += 1

        if len(s_dict) < 2:
            return s

        for key in s_dict:
            v = s_dict[key]
            if len(v) < 2:
                continue
            for i in range(len(v)):
                start = v[i]
                for j in range(len(v) - 1, i, -1):

                    end = v[j]
                    #  print start, end, max
                    if self.checkPalindrome(start, end) == True:
                        if max < end - start + 1:
                            max = end - start + 1
                            index = start
                        break
                    else:
                        if max > end - start + 1:
                            break

        return s[index:index + max]



