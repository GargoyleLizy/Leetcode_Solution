# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        ans = self.trav_Tree(p,q)
        return ans


    def trav_Tree(self,p,q):
        if (p==None) &(q==None):
            return True
        elif (p!=None) &(q!=None):
            if p.val == q.val:
                #print p.left, q.val
                return self.trav_Tree(p.left, q.left) & self.trav_Tree(p.right,q.right)
            else:
                return False
        else:
            return False

solution = Solution()
testp = TreeNode(1)
testp.left = TreeNode(1)
testq = TreeNode(1)

ans = solution.isSameTree(testp,testq)
print ans
