class Solution(object):
    def func(self, num_a, num_b, list, total):
        if total > 0:
            return False

        if num_a == 0 and num_b == 0:
            if total == 0:
                self.result.append(list)
                return True
            else:
                return False

        if num_a > 0:
            self.func(num_a - 1, num_b, list + self.dict["-1"], total - 1)

        if num_b > 0:
            self.func(num_a, num_b - 1, list + self.dict["1"], total + 1)


    def createDict(self):
        self.dict = {}
        self.dict["-1"] = "("
        self.dict["1"] = ")"
        self.result = []


    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.createDict()
        list = ""
        self.func(n, n, list, 0)
        return self.result
