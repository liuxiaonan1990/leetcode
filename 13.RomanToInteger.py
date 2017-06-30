class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rule = {}
        rule["I"] = 1
        rule["V"] = 5
        rule["X"] = 10
        rule["L"] = 50
        rule["C"] = 100
        rule["D"] = 500
        rule["M"] = 1000

        s_list = list(s)
        total = 0
        for i in range(len(s_list)):
            j = i + 1
            if j == len(s_list):
                total += rule[s_list[i]]
            else:
                if rule[s_list[i]] < rule[s_list[j]]:
                    total -= rule[s_list[i]]
                else:
                    total += rule[s_list[i]]

        return total

