class Solution(object):
    def createDict(self):
        self.s_dict = {}
        self.s_dict["("] = -1
        self.s_dict[")"] = 1

    def fillSpace(self, l, r, s):

        while l > 0 and r < len(s):
            if self.s_dict[s[l - 1]] == -1 and self.s_dict[s[r + 1]] == 1:
                self.space[l - 1] = 1
                self.space[r + 1] = 1
                l -= 1
                r += 1

            else:
                return r

        return r

    def findLongest(self, space):
        l = 0
        r = 0
        count = r - l
        ret = count

        flag = False
        for i in range(len(space)):
            if space[i] == 1:
                if flag == False:
                    l = i
                    flag = True
                else:
                    continue

            else:
                if flag == True:
                    r = i
                    flag = False
                    count = r - l
                    if count > ret:
                        ret = count

                else:
                    continue

        if flag == True:
            count = len(space) - l
            if count > ret:
                ret = count

        return ret


    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) < 2:
            return 0

        self.createDict()

        self.space = []
        for i in range(len(s)):
            self.space.append(0)


        i = 0

        while i + 1 < len(s):
            if self.s_dict[s[i]] == -1 and self.s_dict[s[i + 1]] == 1:
                self.space[i] = 1
                self.space[i + 1] = 1
                ret = self.fillSpace(i, i + 1, s)
                print self.space

                i = ret + 1
            else:
                i += 1

        i = 0
        while i + 1 < len(self.space):
            if self.space[i] == 0 and self.space[i + 1] == 1:
                for j in range(i + 2, len(self.space)):
                    if self.space[j] == 1 and self.space[j + 1] == 0:
                        ret = self.fillSpace(i + 1, j, s)
                        print self.space

                        i = ret + 1
                        break

            else:
                i += 1


        return self.findLongest(self.space)





