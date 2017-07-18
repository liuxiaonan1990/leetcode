class Solution(object):
    def createDict(self):
        self.s_dict = {}
        self.s_dict["("] = -1
        self.s_dict[")"] = 1

    def getLen(self, l, r, s):
        length = 0
        total = 0
        i = l
        while i != r:
            total += self.s_dict[s[i]]
            if total == 0:
                length = i - l + 1

            if total > 0:
                return length

            i += 1

        return length

    def getOpposite(self, l, r, s):
        ret = -1
        total = 0
        i = l
        while i != r:
            total += self.s_dict[s[i]]
            if total == 0:
                ret = i
                return ret
            if total < 0:
                continue

        return ret

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        '''
        self.createDict()
        max = 0
        for i in range(len(s)):
            if self.s_dict[s[i]] == -1:
                length = self.getLen(i, len(s), s)
                if length > max:
                    max = length

        return max
        '''
        space = {}
        self.createDict()
        i = 0
        while i < len(s):
            if self.s_dict[s[i]] == -1:
                r = self.getOpposite(i, len(s), s)
                if r == -1:
                    space[i] = -1
                    i += 1
                else:
                    for j in range(i, r + 1):
                        space[j] = 1

                    i = r + 1

            else:
                space[i] = -1
                i += 1

        print len(space)


