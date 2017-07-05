class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """


        if divisor == 0:
            return MAX_INT

        if dividend == 0:
            return 0

        if divisor == 1:
            return dividend



        MAX = 2**31 - 1
        MIN = -2**31

        MAX_INT = MAX

        if divisor == -1:
            if dividend == MIN:
                return MAX_INT
            else:
                return 0 - dividend


        flag = 1
        if dividend < 0 and divisor < 0:
            if dividend > divisor:
                return 0
            dividend = 0 - dividend
            divisor = 0 - divisor

        if dividend > 0 and divisor < 0:
            if dividend < 0 - divisor:
                return 0
            divisor = 0 - divisor
            flag = -1

        if dividend < 0 and divisor > 0:
            if dividend > 0 - divisor:
                return 0
            dividend = 0 - dividend
            flag = -1

        if dividend > 0 and divisor > 0:
            if dividend < divisor:
                return 0


        d_dict = {}

        i = 1
        tmp = divisor

        i_list = [0]
        tmp_list = [0]

        i_list.append(i)
        tmp_list.append(tmp)


        while True:
            i += i
            tmp += tmp

            if tmp > dividend:
                break
            else:
                i_list.append(i)
                tmp_list.append(tmp)

        ret = i_list[-1]
        dividend = dividend - tmp_list[-1]
        for i in range(len(i_list) - 1, 0, -1):
            if dividend - tmp_list[i] == 0:
                ret += i_list[i]
                return ret*flag
            if dividend - tmp_list[i] > 0:
                ret += i_list[i]
                dividend -= tmp_list[i]

            if dividend - tmp_list[i] < 0:
                continue


        return ret*flag





