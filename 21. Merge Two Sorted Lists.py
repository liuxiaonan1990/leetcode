# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)


        p = ListNode(0)
        head = p

        while l1 != None and l2 != None:
            if l1.val  < l2.val:
                p.next = l1
                p = p.next
                l1 = l1.next
            else:
                p.next = l2
                p = p.next
                l2 = l2.next

        while l1 != None:
            p.next = l1
            p = p.next
            l1 = l1.next

        while l2 != None:
            p.next = l2
            p = p.next
            l2 = l2.next

        return head.next
