class Solution(object):

    def findAvailable(self, arr, a, b):

        list_available = []
        for x in range(0, 10):
            list_available.append(str(x))

        for j in range(0, 10):
            if arr[a][j] != ".":
                if arr[a][j] in list_available:
                    list_available.remove(arr[a][j])
                else:
                    return []

        for i in range(0, 10):
            if arr[i][b] != ".":
                if arr[i][b] in list_available:
                    list_available.remove(arr[i][b])
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
                    if arr[i][j] in list_available:
                        list_available.remove(arr[i][j])
                    else:
                        return []


        return list_available

    def checkSuduku(self, arr, a, b):
        list_avail = self.findAvailable(arr, a, b)
        if a == 9 and b == 9 and len(list_avail) == 1:
            return True



    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(0, 10):
            for j in range(0, 10):
                key = board[i][j]
                if key == ".":
                    list_avail = self.findAvailable(board, i, j)
                    if len(list_avail) == 0:
                        return False
                    else:


                else:
                    continue
