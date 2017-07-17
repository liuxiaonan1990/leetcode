class Solution(object):

    def quickSort(self, l, r):
        if l >= r:  # 如果只有一个数字时，结束递归
            return
        flag = l
        for i in range(l + 1, r + 1):  # 默认以第一个数字作为基准数，从第二个数开始比较，生成索引时要注意右部的值
            if self.nums[flag] > self.nums[i]:
                tmp = self.nums[i]
                del self.nums[i]
                self.nums.insert(flag, tmp)
                flag += 1
        self.quickSort(l, flag - 1)  # 将基准数前后部分分别递归排序
        self.quickSort(flag + 1, r)

    def findNextGreater(self, l, r, key):

        ret = -1

        if l > r:
            return ret

        index = l
        greater = self.nums[index]

        for i in range(l, r + 1):
            if self.nums[i] > key and self.nums[i] <= greater:
                index = i
                greater = self.nums[i]
                ret = index

        return ret

    def swap(self, a, b):
        tmp = self.nums[a]
        self.nums[a] = self.nums[b]
        self.nums[b] = tmp



    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """


        self.nums = nums
        l = 0
        r = len(self.nums) - 1

        i = r
        while i >= l:
            key = self.nums[i]
            ret = self.findNextGreater(i + 1, r, key)
            if ret == -1:
                i -= 1
            else:
                self.swap(i, ret)
                self.quickSort(i + 1, r)
                nums = self.nums
                return

        self.quickSort(l, r)
        nums = self.nums
        return






