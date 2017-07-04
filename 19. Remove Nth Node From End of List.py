# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if head.next == None:
            return None

        p1 = ListNode(0)
        p2 = ListNode(0)
        p1.next = head
        p2.next = None

        i = 0
        while p1.next.next != None:
            i += 1
            if i > n:
                p1.next = p1.next.next
                p2.next = p2.next.next
            elif i == n:
                p1.next = p1.next.next
                p2.next = head
            else:
                p1.next = p1.next.next

        if p2.next == None:
            head = head.next
            return head


        p2.next.next = p2.next.next.next


        #print ret.next
        return head