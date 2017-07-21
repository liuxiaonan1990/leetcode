class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        length = len(nums)

        if length == 0:
            return 0
        if length == 1:
            if nums[0] == target:
                return 0
            elif nums[0] > target:
                return 0
            else:
                return 1




        left = 0
        right = length - 1

        while left < right:
            mid = (left + right)/2
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1

            if nums[mid] > target:
                right = mid - 1

        mid = (left + right)/2
        if mid < 0:
            return 0

        if nums[mid] == target:
            return mid
        else:
            if nums[mid] > target:
                return mid
            else:
                return mid + 1
