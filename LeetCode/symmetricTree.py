#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        elif root.left == None and root.right == None:
            return True
        elif root.left != None and root.right != None:
            return self.testSymmetricTreeRec(root.left, root.right)
        else:
            return False

    def testSymmetricTreeRec(self, left, right):
        if left == None and right == None:
            return True
        elif left != None and right != None:
            if left.val == right.val:
                return self.testSymmetricTreeRec(left.left, right.right) and self.testSymmetricTreeRec(left.right,right.left)
            else:
                return False
        else:
            return False

solution = Solution()
test = TreeNode(1)
#test.left = TreeNode(2)
test.right = TreeNode(2)
ans = solution.isSymmetric(test)
print ans
