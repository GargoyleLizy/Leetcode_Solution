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
        res = ListNode(0)
        self.addRec(l1,l2,res,0)
        return res.next

    def addRec(self,l1,l2,res,prog):
        if (l1 == None) &(l2 == None)& (prog == 0) :
            return  
        elif(l1 != None) | (l2 != None) | (prog == 1):
            val1 = 0
            next1 = None
            val2 = 0
            next2 = None
            if( l1 != None):
                val1 = l1.val
                next1 = l1.next
            if(l2 != None):
                val2 = l2.val
                next2 = l2.next
            
            val = val1 + val2 + prog
            res.next = ListNode(val)
            if res.next.val >= 10:
                res.next.val -= 10
                prog = 1
            else:
                prog = 0
            #print next1,next2, res.val, prog
            self.addRec(next1,next2,res.next,prog)

l1 = ListNode(5)
l1_1 = ListNode(2)
l1_2 = ListNode(3)
#l1.next = l1_1
#l1_1.next = l1_2

l2 = ListNode(5)
l2_1 = ListNode(2)
l2_2 = ListNode(3)
#l2.next = l2_1
#l2_1.next = l2_2

solution = Solution()
answ = solution.addTwoNumbers(l1,l2)
while answ != None:
    print answ.val
    answ = answ.next
