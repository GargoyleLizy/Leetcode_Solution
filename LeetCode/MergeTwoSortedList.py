#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return None
        elif l1 ==None :
            return l2
        elif l2 == None:
            return l1
        else:
            if l1.val < l2.val:
                new_head = ListNode(l1.val)
                #print "start stage l1"
                #print new_head.val 
                
                self.mergeRec(new_head, l1.next,l2)
            else :
                new_head = ListNode(l2.val)
                #print "start stage l2"
                #print new_head.val

                self.mergeRec(new_head,l1,l2.next)
        return new_head                 

    def mergeRec(self,prev_node,l1, l2):
        if l1 == None and l2 == None:
            return 
        elif l1 == None:
            prev_node.next = l2
        elif l2 == None:
            prev_node.next = l1
            #print "l2 ends early"
            #print cur_node.val
        else:
            prev_node.next = ListNode(0)
            if l1.val < l2.val:
                prev_node.next.val = l1.val
                #print "Rec stage l1"
                #print prev_node.next.val
                return self.mergeRec(prev_node.next, l1.next, l2)
            else:
                prev_node.next.val = l2.val
                #print "Rec stage l2"
                #print prev_node.next.val, l1.val
                return self.mergeRec(prev_node.next,l1,l2.next)

solution = Solution()
test_l1 = ListNode(1)
test_l1.next = ListNode(3)
test_l2 = ListNode(2)
ans = solution.mergeTwoLists(test_l1,test_l2)
print ans.val, ans.next.next.val
