# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    answ = -1
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        self.explo_Rec(root,1)
        return self.answ
    
    def explo_Rec(self,node,depth):
        if (node != None) :
            if (node.left == None) & (node.right == None):
                if self.answ == -1:
                    self.answ = depth
                elif depth < self.answ:
                    self.answ = depth
                    #print self.answ
                return
            else:
                depth +=1
                if node.left != None:
                    self.explo_Rec(node.left,depth)
                if node.right != None:
                    self.explo_Rec(node.right,depth)
        else:
            self.answ = 0

solution = Solution()
test = TreeNode(0)
test.left = TreeNode(1)
ans = solution.minDepth(test)
print ans
