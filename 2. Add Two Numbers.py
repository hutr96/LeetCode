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

#better solution
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         """
#         Algorithm: Two pointers & math
#         Two pointers for l1 and l2 respectively
#         Math - carry for addition, in the form of new node
#         :param l1: linked list head node
#         :param l2: linked list head node
#         :return: ListNode
#         """
#         result_head = ListNode(0)
#
#         cur1 = l1
#         cur2 = l2
#         cur = result_head
#         while cur1 or cur2:
#             cur.val = cur.val+self.addNode(cur1, cur2)
#             if cur.val < 10:
#                 if cur1 and cur1.next or cur2 and cur2.next:  # next node
#                     cur.next = ListNode(0)
#             else:
#                 cur.val -= 10
#                 cur.next = ListNode(1)
#
#             if cur1:
#                 cur1 = cur1.next
#             if cur2:
#                 cur2 = cur2.next
#             cur = cur.next
#
#         return result_head
#
#     def addNode(self, node1, node2):
#         """
#         Handles None situation
#         :param node1: ListNode
#         :param node2: ListNode
#         :return: integer, summation
#         """
#         if not node1 and not node2:
#             raise Exception("two nodes are None")
#         if not node1:
#             return node2.val
#         if not node2:
#             return node1.val
#         return node1.val+node2.val



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