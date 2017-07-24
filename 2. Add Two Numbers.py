# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):         #Accepted   139ms
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i = 0
        p = l1.val
        q = l2.val
        count1=0
        count2=0
        n = l1
        m = l2
        l3val = []
        carry = 0

        while (p != None) | (q != None):
            if p != None:   #count
                p = n.next
                count1+=1
            if q != None:
                q = m.next
                count2+=1
            n = p
            m = q


            if count1 == count2:    #calculation
                val = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif count1 > count2:
                val = l1.val
                l1 = l1.next
            elif count2 > count1:
                val = l2.val
                l2 = l2.next
            if carry == 1:
                val+=1
                carry = 0
            if val >= 10:
                val = val-10
                carry = 1
            l3val.append(val)


            Sum = ListNode(l3val[i])
            if i == 0 :
                l3s = Sum
                l3 = l3s
            else :
                l3s.next = Sum
                l3s = l3s.next

            i+=1

        if carry == 1:
            l3s.next = ListNode(1)

        return l3





if __name__ == "__main__":
    Solution=Solution()
    l1 = ListNode(2)        #Test
    n = l1
    n.next = ListNode(4)
    n = n.next
    n.next = ListNode(6)
    n = n.next

    l2 = ListNode(5)
    n = l2
    n.next = ListNode(6)
    n = n.next
    n.next = ListNode(4)
    n = n.next

    ans = Solution.addTwoNumbers(l1,l2)
    print ans.val
    while ans.next!=None:
        ans = ans.next
        print ans.val