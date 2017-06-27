class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a1 = 0
        a2 = 0
        p1 = l1
        i = 0
        while True:
            a1 += p1.val * (10 ** i)
            if p1.next != None:
                p1 = p1.next
                i += 1
            else:
                break
        print a1

        p2 = l2
        i = 0
        while True:
            a2 += p2.val * (10 ** i)
            if p2.next != None:
                p2 = p2.next
                i += 1
            else:
                break
        print a2

        a3 = a1 + a2
        x = 0
        y = 0
        z = 10

        p3 = ListNode(0)
        pHead = p3
        while True:
            x = a3 / z
            y = a3 % z

            node = ListNode(y)
            p3.next = node
            p3 = node

            if x == 0:
                return pHead.next
            else:
                a3 = x