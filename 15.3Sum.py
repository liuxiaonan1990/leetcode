class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        num_dict = {}
        for i in range(len(nums)):
            if num_dict.has_key(nums[i]) == False:
                num_dict[nums[i]] = 1
            else:
                num_dict[nums[i]] += 1

        num_list = num_dict.keys()
        num_list.sort()

        ret = []

        for i in range(0, len(num_list)):
            if num_list[i] == 0 and num_dict[0] > 2:
                tuple = [0, 0, 0]
                ret.append(tuple)
                continue

            if num_list[i] == 0 and num_dict[0] == 2:
                continue

            if num_dict[num_list[i]] > 1:
                start_pos = i
            else:
                start_pos = i + 1
            for j in range(start_pos, len(num_list)):

                key = 0 - num_list[i] - num_list[j]

                if key < num_list[j]:
                    break
                if key == num_list[j]:
                    if num_dict[key] > 1:
                        tuple = [num_list[i], num_list[j], key]
                        ret.append(tuple)
                        continue
                    else:
                        continue

                if num_dict.has_key(key):
                    tuple = [num_list[i], num_list[j], key]
                    ret.append(tuple)

        return ret


