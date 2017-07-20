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

            if len(s) - i < 0 - total:
                return length

            i += 1

        return length

    def getOpposite(self, l, r, s):

  #      print l, r

        ret = -1
        total = 0
        i = l

        first_right = -1
        flag = False
        while i != r:
            if self.s_dict[s[i]] == 1 and flag == False:
                flag = True
                first_right = i

            total += self.s_dict[s[i]]
            if total == 0:
                ret = i
                return [ret, total, first_right]
            if total < 0:
                i += 1
                continue


        return [ret, total, first_right]

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
                ret = self.getOpposite(i, len(s), s)
          #      print ret
                r = ret[0]

                if r == -1:
                    total = ret[1]
                    first_right = ret[2]
                    if first_right == -1:
                        for j in range(i, len(s)):
                            space[j] = -1

                        break
                    else:
                        if first_right - i > 0 - total:
                            for j in range(i, i + 0 - total):
                                space[j] = -1

                            i += 0 - total
                        else:
                            for j in range(i, first_right - 1):
                                space[j] = -1

                            i = first_right - 1


                else:
                    for j in range(i, r + 1):
                        space[j] = 1

                    i = r + 1

            else:
                space[i] = -1
                i += 1

    #    print len(space)

        return self.findLongest(space)



