# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        vals = []
        vals = self.traversalRec([root],vals)
        return vals

    def traversalRec(self,nodes,vals):
        next_level_nodes= []
        level_vals = []
        for node in nodes:
            if node != None:
                next_level_nodes.append(node.left)
                next_level_nodes.append(node.right)
                level_vals.append(node.val)

        if next_level_nodes == []:
            return vals
        else:
            vals = [level_vals] + vals
            return self.traversalRec(next_level_nodes,vals)
solution = Solution()
test = TreeNode(1)
test.left = TreeNode(2)
test.right = TreeNode(3)
test.right.right = TreeNode(4)
ans = solution.levelOrderBottom(test)
print ans
