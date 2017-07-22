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


    def checkSuduku(self, arr, a, b):
        pos = self.findNext(arr, a, b)
        if pos[0] == -1 and pos[1] == -1:
            return True

        a = pos[0]
        b = pos[1]

        list_avail = self.findAvailable(arr, a, b)

        if a == 8 and b == 8 and len(list_avail) == 1:
            return True

        if len(list_avail) == 0:
            return False

        for x in range(len(list_avail)):
            arr[a][b] = list_avail[x]
            r = self.checkSuduku(arr, a, b)
            if r == True:
                return True
            else:
                continue

        return False


    def checkValid(self, arr, a, b):

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
                    return False

        for i in range(0, 9):
            if arr[i][b] != ".":
                if arr[i][b] in list_col:
                    list_col.remove(arr[i][b])
                else:
                    return False

        if a >= 0 and a <= 2:
            x = 0
        elif a >= 3 and a <= 5:
            x = 1
        else:
            x = 2

        if b >= 0 and b <= 2:
            y = 0
        elif b >= 3 and b <= 5:
            y = 1
        else:
            y = 2

        for i in range(0 + 3 * x, 3 + 3 * x):
            for j in range(0 + 3 * y, 3 + 3 * y):
                if arr[i][j] != ".":
                    if arr[i][j] in list_nine:
                        list_nine.remove(arr[i][j])
                    else:
                        return False
   #     print a, b, list_row, list_col, list_nine
        return True


    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

 #       for i in range(0, 9):
 #           print board[i]

        list = [[0, 0], [1, 3], [2, 6], [3, 1], [4, 4], [5, 7], [6, 2], [7, 5], [8, 8]]

        for i in range(len(list)):
            a = list[i][0]
            b = list[i][1]
            if self.checkValid(board, a, b) == False:
                return False


        return True