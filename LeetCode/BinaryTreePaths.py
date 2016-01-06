# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = []
        if root == None:
            pass
        elif root.left == None and root.right == None:
            ans.append(str(root.val))
        else:
            if root.left != None:
                self.deep_first_rec(root.left,str(root.val),ans)
            if root.right != None:
                self.deep_first_rec(root.right, str(root.val),ans)
        return ans

    def deep_first_rec(self, node, path_str,ans):
        path_str += "->" + str(node.val)
        print path_str
        if node.left == None and node.right ==None:
            ans.append(path_str)
        else:
            if node.left != None:
                self.deep_first_rec(node.left, path_str,ans)
            if node.right != None:
                self.deep_first_rec(node.right, path_str,ans)

solution = Solution()
test = TreeNode(1)
test.left = TreeNode(2)
ans = solution.binaryTreePaths(None)
print ans
