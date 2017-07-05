# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def merge2Lists(self, l1, l2):
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

    def mergeKLists_old(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return lists

        if len(lists) == 1:
            return lists[0]

        head = lists[0]

        for i in range(1, len(lists)):
            head = self.merge2Lists(head, lists[i])


        return head


    def func(self, lists):

        ret = []
        if len(lists) < 2:
            return lists

        i = 0
        while i < len(lists):
            if i + 1 < len(lists):
                l = self.merge2Lists(lists[i], lists[i + 1])
                ret.append(l)
                i += 2
            else:
                ret.append(lists[i])
                break

        return ret

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        ret = lists
        while len(ret) > 1:
            ret = self.func(ret)

        if len(ret) == 0:
            return ret
        if len(ret) == 1:
            return ret[0]

        return ret




