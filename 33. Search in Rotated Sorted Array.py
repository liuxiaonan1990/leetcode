class Solution(object):
    def halfFind(self, list, left, right, target):
        l = left
        r = right
        mid = (l + r)/2
        while l < r:
            mid = (l + r)/2
 #           print l, r

            if list[mid] == target:
                return mid
            if list[mid] > target:
                r = mid - 1
            if list[mid] < target:
                l = mid + 1

        mid = (l + r)/2
        if list[mid] == target:
            return mid
        else:
            return -1


    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1




        length = len(nums)

        if nums[0] < nums[length - 1]:
            return self.halfFind(nums, 0, length - 1, target)


        total = length
        i = 0
        while i < length:
            if nums[i] > nums[total - 1]:
                nums.append(nums[i])
                total += 1
                i += 1
            else:
                break

  #      print nums

        ret = self.halfFind(nums, i, total - 1, target)
        if ret == -1:
            return ret
        if ret >= length:
            return ret - length
        else:
            return ret