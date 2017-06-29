class Solution(object):
    # split p => abc
    #           a.c
    #           a*
    #           .*
    def split_expression(self, p):
        self.p_list = []
        self.p_list = list(p)
        self.split_list = []

        last = 0
        pos = 0

        for i in range(0, len(self.p_list)):
            if self.p_list[i] == "*":
                if i == last:
                    return -1
                else:
                    p1_start = last
                    p1_end = i - 1
                    p2_start = i - 1
                    p2_end = i + 1
                    p1 = self.p_list[p1_start:p1_end]
                    p2 = self.p_list[p2_start:p2_end]
                    # print p2
                    last = i + 1

                    if len(p1) != 0:
                        self.split_list.append(p1)

                    self.split_list.append(p2)


        self.split_list_new = []
        p1 = self.p_list[last:]
        if len(p1) != 0:
            self.split_list.append(p1)

        '''
        p_last = []
        for i in range(len(self.split_list)):
            v = self.split_list[i]
            if "*" in v and "*" in p_last:
                if p_last == ['.', '*'] or v == ['.', '*']:
                    p_last = ['.', '*']
                    if len(self.split_list_new) > 0:
                        self.split_list_new.pop()
                    self.split_list_new.append(p_last)

                elif p_last == v:
                    continue
                else:
                    self.split_list_new.append(v)
                    p_last = v
            else:
                self.split_list_new.append(v)
                p_last = v
        '''

        #stack for a*, .*
        p_last = []
        for i in range(len(self.split_list)):
            v = self.split_list[i]
            if v == ['.', '*']:
                p_last = []
                p_last.append(v)
            elif "*" in v:
                if len(p_last) > 0:
                    top = p_last.pop()

                    if top == ['.', '*']:
                        p_last.append(top)
                        continue
                    elif top == v:
                        p_last.append(top)
                        continue
                    else:
                        p_last.append(top)
                        p_last.append(v)
                else:
                    p_last.append(v)
            else:
                if p_last != []:
                    self.split_list_new += p_last
                    p_last = []
                self.split_list_new.append(v)

        if p_last != []:
            self.split_list_new += p_last





        return 0

    def check(self, s_list, p_list):
    #    print "check"
    #    print s_list
    #    print p_list
        if len(s_list) == 0 and len(p_list) == 0:
            return True

        if len(s_list) == 0:

            '''
            if len(p_list[0]) == 2 and p_list[0][1] == "*" and len(p_list) == 1:
                return True
            else:
                return False
            '''

            for i in range(len(p_list)):
                v = p_list[i]
                if "*" in v :
                    continue
                else:
                    return False

            return True

        if len(s_list) != 0 and len(p_list) == 0:
            return False




        p_current = p_list[0]
        p_current_len = len(p_current)

        if p_current_len == 2 and p_current[0] == "." and p_current[1] == "*":
            if self.check(s_list[1:], p_list[0:]) == False and \
                            self.check(s_list[1:], p_list[1:]) == False and \
                            self.check(s_list[0:], p_list[1:]) == False:
                return False
            else:
                return True
        # a*
        elif p_current_len == 2 and p_current[0] != "." and p_current[1] == "*":
            # first char same
            if s_list[0] == p_current[0]:
                if self.check(s_list[1:], p_list[0:]) == False and\
                                self.check(s_list[1:],p_list[1:]) == False and\
                                self.check(s_list[0:], p_list[1:]) == False:
                    return False
                else:
                    return True
            # first char not same
            else:
                if self.check(s_list[0:], p_list[1:]) == True:
                    return True
                else:
                    return False

        else:
            if len(s_list) < p_current_len:
                return False
            else:
                s_current = s_list[0:p_current_len]
                for i in range(0, p_current_len):
                    if p_current[i] == ".":
                        continue
                    elif s_current[i] == p_current[i]:
                        continue
                    else:
                        return False

                return self.check(s_list[p_current_len:], p_list[1:])

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ret = self.split_expression(p)
        if ret == -1:
            return False

        print self.split_list_new

        s_list = list(s)
        return self.check(s_list, self.split_list_new)

