# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    answ = 0
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #answ=-1
        self.explo_Rec(root,0)
        return self.answ
    
    def explo_Rec(self,node,depth):
        if node == None:
            if depth > self.answ:
                self.answ = depth
                #print self.answ
            return
        else:
            depth +=1
            self.explo_Rec(node.left,depth)
            self.explo_Rec(node.right,depth)

solution = Solution()
test = TreeNode(0)

answ = solution.maxDepth(test)
print answ

