class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        List = []
        for i in range(len(nums)):
            value = nums[i]
            dict[value] = i

        for i in range(len(nums)):
            another = target - nums[i]
            if dict.has_key(another):
                if dict[another] == i:
                    continue
                else:
                   List.append(i)
                   List.append(dict[another])
                   return List

