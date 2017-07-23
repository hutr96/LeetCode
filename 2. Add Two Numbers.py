# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i = 0
        j = l1.val
        count=0
        n = l1
        while j != None:
            j = n.next
            n = j
            count+=1
        #print "count = %f" % count


        l3val = []
        # l1s = l1
        # l2s = l2

        while i < count:

            val = l1.val + l2.val
            if val >= 10:
                val = val-10
            l3val.append(val)
            l1 = l1.next
            l2 = l2.next
            l3s = ListNode(l3val[i])
            if i == 0 :
                l3 = l3s
            l3s = l3s.next
            i+=1
        return l3





if __name__ == "__main__":
    Solution=Solution()
    l1 = ListNode(3)
    n = l1
    n.next = ListNode(6)
    n = n.next
    n.next = ListNode(4)
    n = n.next

    l2 = ListNode(5)
    n = l2
    n.next = ListNode(4)
    n = n.next
    n.next = ListNode(3)
    n = n.next

    print Solution.addTwoNumbers(l1,l2)