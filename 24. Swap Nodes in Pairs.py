# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def func(self, l):
        p = l
        if p == None:
            return p

        if p.next == None:
            return p

        tmp = p.next
        p.next = self.func(tmp.next)
        tmp.next = p
        return tmp


    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.func(head)


