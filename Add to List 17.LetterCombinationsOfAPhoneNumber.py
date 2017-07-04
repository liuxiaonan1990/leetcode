class Solution(object):

    def createDict(self):

        self.mapDict = {}
        self.mapDict["1"] = "*"
        self.mapDict["2"] = ['a', 'b', 'c']
        self.mapDict["3"] = ['d', 'e', 'f']
        self.mapDict["4"] = ['g', 'h', 'i']
        self.mapDict["5"] = ['j', 'k', 'l']
        self.mapDict["6"] = ['m', 'n', 'o']
        self.mapDict["7"] = ['p' , 'q', 'r', 's']
        self.mapDict["8"] = ['t', 'u', 'v']
        self.mapDict["9"] = ['w', 'x', 'y', 'z']
        self.mapDict["0"] = [' ']

    def func_mult(self, a, b):
        c_list = []
        for i in range(len(a)):
            for j in range(len(b)):
                c = a[i] + b[j]
                c_list.append(c)

        return c_list

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        self.createDict()

        c_list = []
        if len(digits) == 0:
            return c_list

        c_list = self.mapDict[digits[0]]

        if len(digits) == 1:
            return c_list

        for i in range(1, len(digits)):
            num_str = self.mapDict[digits[i]]
            c_list = self.func_mult(c_list, num_str)

        return c_list







