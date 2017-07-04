class Solution(object):

    def createDict(self):
        self.dict = {}
        self.dict["("] = -1
        self.dict[")"] = 1
        self.dict["["] = -2
        self.dict["]"] = 2
        self.dict["{"] = -3
        self.dict["}"] = 3


    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        self.createDict()
        s_list = list(s)
        stack = []

        while len(s_list) > 0:
            i = len(s_list) - 1
            key = s_list[i]
            #print key, s_list
            val = self.dict[key]
            if val > 0:
                stack.append(key)
                del s_list[i]
            if val < 0:
                if len(stack) < 1:
                    return False

                op = stack[-1]
                if val + self.dict[op] == 0:
                    del stack[-1]
                    del s_list[i]
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False




