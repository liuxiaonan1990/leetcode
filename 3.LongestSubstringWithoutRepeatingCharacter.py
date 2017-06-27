class ListNode(object):
    def __init__(self, max, last):
        self.max = max
        self.last = last



class Solution(object):


    def getMax(self, s_list):
        dict_s = {}
        total_max = 0
        for i in range(len(s_list)):
            c = s_list[i]
            if dict_s.has_key(c):
                v = dict_s[c]
                if i - v.last > v.max:
                    v.max = i - v.last
                    v.last = i
                    if total_max < v.max:
                        total_max = v.max
                else:
                    v.last = i

                dict_s[c] = v
            else:
                v = ListNode(0, i)
                dict_s[c] = v

        for key in dict_s:
            v = dict_s[key]
            if len(s_list) - v.last > v.max:
                v.max = len(s_list) - v.last
                if total_max < v.max:
                    total_max = v.max

        return total_max




    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list = list(s)

        total_max = self.getMax(s_list)

        max = 0
        max_pos = 0
        i = 0
        while i < len(s_list):
            dict_s = {}

            j = 0
            for j in range(i, len(s_list)):
                if dict_s.has_key(s_list[j]):
                    if j - i > max:
                        max = j - i
                        max_pos = j
                        print max

                        if max == total_max:
                            return max
                    else:
                        if j < max_pos:
                            i = j - 1

                    break
                else:
                    dict_s[s_list[j]] = True

            if len(dict_s) == len(s_list) - i:
                if max < len(dict_s):
                    max = len(dict_s)
                    print max
                    if max == total_max:
                        return max

            i += 1


        return max