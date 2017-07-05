class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 2:
            return len(nums)

        tmp = nums[0]
        total_len = 1

        last = nums[-1]

        i = 1
        while True:
            if nums[i] == last:
                if nums[i] == tmp:
                    return total_len
                else:
                    total_len += 1
                    return total_len
            else:
                if nums[i] == tmp:
                    del nums[i]
                else:
                    tmp = nums[i]
                    i += 1
                    total_len += 1


        return total_len