class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        ret = -1
        for i in range(0, len(haystack) - len(needle) + 1):
            flag = True
            for j in range(0, len(needle)):
                if haystack[i + j] == needle[j]:
                    continue
                else:
                    flag = False
                    break

            if flag == True:
                ret = i
                break

        return ret
