class Solution(object):
    #折半查找
    def findClosest(self, target, num_list):

        i = 0
        j = len(num_list) - 1

        if target < num_list[i]:
            return i
        if target > num_list[j]:
            return j

        mid = (i + j)/2
        while i <= j:
            if target > num_list[mid]:
                i = mid + 1
                mid = (i + j)/2

            elif target < num_list[mid]:
                j = mid - 1
                mid = (i + j) / 2

            else:
                return mid

        if num_list[mid] > target:

            if mid - 1 >= 0:

                if num_list[mid] - target < target - num_list[mid - 1]:
                    return mid
                else:
                    return mid - 1

            else:
                return mid

        if num_list[mid] < target:
            if mid + 1 < len(num_list):
                if num_list[mid + 1] - target < target - num_list[mid]:
                    return mid + 1
                else:
                    return mid
            else:
                return mid


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

        min = a + b + c

        if num_dict[b] == 0:
            num_list.insert(i, b)
            num_dict[b] += 1
        else:
            num_dict[b] += 1

        if num_dict[a] == 0:
            num_list.insert(i, a)
            num_dict[a] += 1
        else:
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
        max = a + b + c



        if num_dict[b] == 0:
            num_list.append(b)
            num_dict[b] += 1
        else:
            num_dict[b] += 1

        if num_dict[a] == 0:
            num_list.append(a)
            num_dict[a] += 1
        else:
            num_dict[a] += 1


        return max



    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        num_dict = {}
        for i in range(len(nums)):
            if num_dict.has_key(nums[i]) == False:
                num_dict[nums[i]] = 1
            else:
                num_dict[nums[i]] += 1

        num_list = num_dict.keys()
        num_list.sort()

        min = abs(target - (nums[0] + nums[1] + nums[2]))
        result = nums[0] + nums[1] + nums[2]

        list_max = self.getMax(num_list, num_dict)
        list_min = self.getMin(num_list, num_dict)

        print list_max, list_min
        if target >= list_max:
            return  list_max
        if target <= list_min:
            return  list_min


        for i in range(0, len(num_list)):

            a = num_list[i]
            num_dict[num_list[i]] -= 1
            if num_dict[num_list[i]] == 0:
                #num_list.remove(num_list[i])
                del num_list[i]
                start_pos = i
            else:
                start_pos = i

            #out of range
            if start_pos == len(num_list):
                break

            for j in range(start_pos, len(num_list)):

                b = num_list[j]
                num_dict[num_list[j]] -= 1
                if num_dict[num_list[j]] == 0:
                    #num_list.remove(num_list[j])
                    del num_list[j]

                #out of range
                if j == len(num_list):
                    if num_dict[b] == 0:
                        num_list.insert(j, b)

                    num_dict[b] += 1

                    if num_dict[a] == 0:
                        num_list.insert(i, a)

                    num_dict[a] += 1

                    break

                key = target - a - b

                #print a, b, key

                if key < b:
                    key = num_list[j]
                    ret = abs(target - a - b - key)
                    if ret <= min:
                        min = ret
                        result = a + b + key
                        if min == 0:
                            return result

                    if num_dict[b] == 0:
                        num_list.insert(j, b)

                    num_dict[b] += 1
                    break

                else:
                    index = self.findClosest(key, num_list)
                    key = num_list[index]


                    ret = abs(target - a - b - key)
                    if ret <= min:
                        min = ret
                        result = a + b + key
                        if min == 0:
                            return result

                    if num_dict[b] == 0:
                        num_list.insert(j, b)

                    num_dict[b] += 1
                 #   print num_list, num_dict

       #     print num_list, num_dict, i
            if num_dict[a] == 0:
                num_list.insert(i, a)

            num_dict[a] += 1



        return result


