# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def checkLen(self, l, n):
        i = 0
        while l != None:
            i += 1
            if i == n:
                return True

            l = l.next

        if i < n:
            return False



    def convert(self, l, n):

        head = l

        if self.checkLen(head, n) == False:
            return l


        head = l
        p = l
        i = 0

        if head == None:
            return head

        while p.next != None:
            i += 1
            if i == n:
                break

            tmp = p.next
            p.next = tmp.next
            tmp.next = head
            head = tmp

        if p.next == None:
            return head
        else:
            p.next = self.convert(p.next, n)
            return head




    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """


        return  self.convert(head, k)

