class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        min_len = len(strs[0])
        min_str = strs[0]
        for i in range(len(strs)):
            if len(strs[i]) == 0:
                return ""

            if len(strs[i]) < min_len:
                min_len = len(strs[i])
                min_str = strs[i]


        for j in range(len(strs)):
            for p in range(0, min_len):
                if strs[j][p] != min_str[p]:
                    min_len = p
                    break
                else:
                    continue

        return min_str[0:min_len]