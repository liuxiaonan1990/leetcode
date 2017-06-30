class Solution(object):
    def createRule(self):
        self.rule = {}
        for i in range(0, 4):
            one = ""
            five = ""
            ten = ""
            if i == 0:
                one = "I"
                five = "V"
                ten = "X"
            if i == 1:
                one = "X"
                five = "L"
                ten = "C"
            if i == 2:
                one = "C"
                five = "D"
                ten = "M"
            if i == 3:
                one = "M"
                five = ""
                ten = ""

            for j in range(1, 10):
                key = j * (10 ** i)

                if key > 3999:
                    return

                if j == 1:
                    val = one
                if j == 2:
                    val = one + one
                if j == 3:
                    val = one + one + one
                if j == 4:
                    val = one + five
                if j == 5:
                    val = five
                if j == 6:
                    val = five + one
                if j == 7:
                    val = five + one + one
                if j == 8:
                    val = five + one + one + one
                if j == 9:
                    val = one + ten
                if j == 10:
                    val = ten

                self.rule[key] = val

        return

    def split(self, num):
        self.num_list = []

        for i in range(1, 5):
            b = 10
            a = num % b
            num = num / b

            if a != 0:
                self.num_list.insert(0, a * ( b**(i-1) ) )

            if num == 0:
                return
            else:
                continue




    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 1 or num > 3999:
            return ""

        self.createRule()
        #print self.rule

        self.split(num)
        #print self.num_list

        s = ""
        for i in range(len(self.num_list)):
            s += self.rule[self.num_list[i]]

        return s


