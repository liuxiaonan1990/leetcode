class Solution(object):
    def getMin(self, num_list, num_dict):

        i = 0
        a = num_list[i]

        num_dict[a] -= 1
        if num_dict[a] == 0:
            del num_list[i]

        b = num_list[i]
        num_dict[b] -= 1
        if num_dict[b] == 0:
            del num_list[i]

        c = num_list[i]
        num_dict[c] -= 1
        if num_dict[c] == 0:
            del num_list[i]

        d = num_list[i]

        min = a + b + c + d

        if num_dict[c] == 0:
            num_list.insert(i, c)

        num_dict[c] += 1

        if num_dict[b] == 0:
            num_list.insert(i, b)

        num_dict[b] += 1

        if num_dict[a] == 0:
            num_list.insert(i, a)

        num_dict[a] += 1

        return min

    def getMax(self, num_list, num_dict):
        i = len(num_list) - 1
        a = num_list[i]

        num_dict[a] -= 1
        if num_dict[a] == 0:
            del num_list[i]

        i = len(num_list) - 1
        b = num_list[i]
        num_dict[b] -= 1
        if num_dict[b] == 0:
            del num_list[i]

        i = len(num_list) - 1
        c = num_list[i]
        num_dict[c] -= 1
        if num_dict[c] == 0:
            del num_list[i]

        i = len(num_list) - 1
        d = num_list[i]

        max = a + b + c + d

        if num_dict[c] == 0:
            num_list.append(c)

        num_dict[c] += 1


        if num_dict[b] == 0:
            num_list.append(b)

        num_dict[b] += 1

        if num_dict[a] == 0:
            num_list.append(a)

        num_dict[a] += 1

        return max

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
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

        result = []

        if len(nums) < 4:
            return result


        list_max = self.getMax(num_list, num_dict)
        list_min = self.getMin(num_list, num_dict)
        
        
        
        print list_max, list_min
        if target > list_max or target < list_min:
            return result



        for i in range(0, len(num_list)):

            a = num_list[i]
            num_dict[num_list[i]] -= 1
            if num_dict[num_list[i]] == 0:
                del num_list[i]

            start_b = i
            # out of range
            if start_b == len(num_list):
                break

            for j in range(start_b, len(num_list)):

                b = num_list[j]
                num_dict[num_list[j]] -= 1
                if num_dict[num_list[j]] == 0:
                    del num_list[j]

                start_c = j
                # out of range
                if start_c == len(num_list):
                    if num_dict[b] == 0:
                        num_list.insert(j, b)

                    num_dict[b] += 1

                    if num_dict[a] == 0:
                        num_list.insert(i, a)

                    num_dict[a] += 1

                    break

                for x in range(start_c, len(num_list)):
                    c = num_list[x]

                    num_dict[num_list[x]] -= 1
                    if num_dict[num_list[x]] == 0:
                        del num_list[x]

                    key = target - a - b - c

                    if key < c:
                        if num_dict[c] == 0:
                            num_list.insert(x, c)

                        num_dict[c] += 1
                        break

                    if key in num_list:
                        result.append([a, b, c, key])

                    if num_dict[c] == 0:
                        num_list.insert(x, c)

                    num_dict[c] += 1

                ######################
                if num_dict[b] == 0:
                    num_list.insert(j, b)

                num_dict[b] += 1

            ######################
            if num_dict[a] == 0:
                num_list.insert(i, a)

            num_dict[a] += 1




        return result
