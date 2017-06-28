class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        s_list = list(s)
        total_len = len(s)
        p_src = 0
        p_dst = 0
        d_list = []

        if numRows < 2:
            return s

        for i in range(0, numRows):
            j = 0
           # while (2 * numRows - 2) * j + i < total_len and (2 * numRows - 2) * j + (2 * numRows + 2) - i < total_len:
            while True:
                index = (2*numRows-2)*j + i
                if index < total_len:
                    d_list.append(s_list[index])
                else:
                    break

                if i == 0 or i == numRows - 1:
                    j += 1

                else:
                    index = (2*numRows-2)*j + (2*numRows-2) - i
                    if index < total_len:
                        d_list.append(s_list[index])
                    else:
                        break

                    j += 1

        str = "".join(d_list)

        return str




