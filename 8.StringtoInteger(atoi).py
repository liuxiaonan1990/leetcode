class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        v = " "
        space_list = str.split(" ")
        for i in range(len(space_list)):
            v = space_list[i]
            if v != "":
                break

        s_list = list(v)
        NUM = {}
        NUM["0"] = 0
        NUM["1"] = 1
        NUM["2"] = 2
        NUM["3"] = 3
        NUM["4"] = 4
        NUM["5"] = 5
        NUM["6"] = 6
        NUM["7"] = 7
        NUM["8"] = 8
        NUM["9"] = 9

        x = 0
        flag = 1
        m = 10
        for i in range(len(s_list)):

            if NUM.has_key(s_list[i]) == False:


                if i > 0:

                    if x*flag > 2**31-1:
                        return 2**31-1
                    elif x*flag < -2**31:
                        return -2**31
                    else:
                        return x*flag
                else:
                    if s_list[i] == "+":
                        flag = 1
                    elif s_list[i] == "-":
                        flag = -1
                    else:
                        return 0


            else:
                x = x * m + NUM[s_list[i]]


        if x*flag > 2**31 - 1:
            return 2 ** 31 - 1
        elif x * flag < -2 ** 31:
            return -2 ** 31
        else:
            return x * flag
