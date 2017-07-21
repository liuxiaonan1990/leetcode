class Solution(object):
    def findSame(self, nums, index):
        target = nums[index]
        l = index
        r = index
        while nums[l] == target:
            l -= 1
            if l < 0:
                break

        l += 1

        while nums[r] == target:
            r += 1
            if r > len(nums) - 1:
                break

        r -= 1
        return [l, r]


    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        length = len(nums)

        if length == 0:
            return [-1, -1]
        if length == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]


        left = 0
        right = length - 1

        while left < right:
            mid = (left + right)/2
            if nums[mid] == target:
                return self.findSame(nums, mid)

            if nums[mid] < target:
                left = mid + 1

            if nums[mid] > target:
                right = mid - 1

        mid = (left + right)/2
        if nums[mid] == target:
            return self.findSame(nums, mid)
        else:
            return [-1, -1]