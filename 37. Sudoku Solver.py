class Solution(object):

    def findAvailable(self, arr, a, b):

        list_available = []
        list_row = []
        list_col = []
        list_nine = []
        for x in range(1, 10):
            list_row.append(str(x))
            list_col.append(str(x))
            list_nine.append(str(x))


        for j in range(0, 9):
            if arr[a][j] != ".":
                if arr[a][j] in list_row:
                    list_row.remove(arr[a][j])
                else:
                    return []

        for i in range(0, 9):
            if arr[i][b] != ".":
                if arr[i][b] in list_col:
                    list_col.remove(arr[i][b])
                else:
                    return []

        if a >=0 and a <=2:
            x = 0
        elif a >= 3 and a <=5:
            x = 1
        else:
            x = 2

        if b >=0 and b <=2:
            y = 0
        elif b >=3 and b <=5:
            y = 1
        else:
            y = 2

        for i in range(0+3*x, 2+3*x):
            for j in range(0+3*y, 2+3*y):
                if arr[i][j] != ".":
                    if arr[i][j] in list_nine:
                        list_nine.remove(arr[i][j])
                    else:
                        return []
        for i in range(len(list_row)):
            if list_row[i] in list_col and list_row[i] in list_nine:
                list_available.append(list_row[i])

        return list_available

    def findNext(self, arr, a, b):
        if a == 8 and b == 8 and arr[a][b] != ".":
            return [-1, -1]

        if arr[a][b] != ".":
            if b != 8:
                b += 1
            else:
                a += 1
                b = 0

            return self.findNext(arr, a, b)

        else:
            return [a, b]


    def checkSuduku(self, a, b):
        pos = self.findNext(self.arr, a, b)
        if pos[0] == -1 and pos[1] == -1:
            return True

        a = pos[0]
        b = pos[1]
        print a, b, self.arr

        list_avail = self.findAvailable(self.arr, a, b)

        if a == 8 and b == 8 and len(list_avail) == 1:
            self.arr[a][b] = list_avail[0]
            return True

        if len(list_avail) == 0:
            self.arr[a][b] = "."
            return False

        for x in range(len(list_avail)):
            self.arr[a][b] = list_avail[x]
            r = self.checkSuduku(a, b)
            if r == True:
                return True
            else:
                pass

        self.arr[a][b] = "."
        return False

    def count9area(self):
        self.areacount = dict()
        for x in range(0, 9):
            a = x / 3
            b = x % 3

            start_row = a * 3
            start_col = b * 3

            count = 0
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if self.arr[i][j] == '.':
                        count += 1

            self.areacount[x] = count





    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        self.arr = board
        arr =  self.checkSuduku(0, 0)
        if arr != False:
            board = self.arr
            return