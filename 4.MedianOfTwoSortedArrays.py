class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = 0
        j = 0
        len1 = len(nums1)
        len2 = len(nums2)
        new_num = []
        p = 0
        while i < len1 and j < len2:
            if nums1[i] <= nums2[j]:
                new_num.append(nums1[i])
                p += 1
                i += 1
            else:
                new_num.append(nums2[j])
                p += 1
                j += 1

        if i == len1:
            while j < len2:
                new_num.append(nums2[j])
                p += 1
                j += 1
        else:
            while i < len1:
                new_num.append(nums1[i])
                p += 1
                i += 1
        print p
        if p % 2 == 1:
            return new_num[p/2]
        else:
            return (new_num[p/2] + new_num[p/2 - 1])/2.0


