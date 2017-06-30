class Solution(object):
    #filter (a[i] > a[i - 1]) == False
    #filter (a[j] > a[j + 1]) == False
    #def filter(self, height):


    def min(self, a, b):
        if a < b:
            return a
        else:
            return b

    def max(self, a, b):
        if a < b:
            return b
        else:
            return a

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max = 0
        start_high = 0


        highest = height[0]
        highest_index = 0
        for i in range(len(height)):
            if height[i] > highest:
                highest  = height[i]
                highest_index = i

        if highest_index == 0:
            for j in range(highest_index + 1, len(height)):
                s = (j - highest_index) * height[j]
                if s > max:
                    max = s

            return max

        elif highest_index == len(height) - 1:
            for i in range(0, highest_index):
                s = (highest_index - i) * height[i]
                if s > max:
                    max = s
            return max

        else:

            for i in range(len(height)):
                if i > 0:
                    if height[i] < height[i - 1]:
                        continue

                if height[i] < start_high:
                    continue
                if (len(height) - 1 - i) * self.min(highest, height[i]) < max:
                    continue

                for j in range(len(height) - 1, i, -1):
                    s = (j - i) * self.min(height[i], height[j])
                    if s > max:
                        max = s
                        start_high = height[i]

            return max