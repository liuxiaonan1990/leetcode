class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        if len(nums) == 0:
            return len(nums)

        total_len = 0

        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                total_len += 1
                i += 1

        return total_len

