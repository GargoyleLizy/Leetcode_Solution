class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        k = set()
        for elt in nums:
            if elt in k:
                return True
            else:
                k.add(elt)
        return False

test = [1,2,3,1]
solution = Solution()
ans = solution.containsDuplicate(test)
print ans
