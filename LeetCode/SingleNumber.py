class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mid_val = 0
        num_set = set()
        for elt in nums:
            if elt in num_set:
                mid_val -= elt
            else:
                mid_val += elt
                num_set.add(elt)
        return mid_val

solution = Solution()
test = [1,1,2,3,3]
ans = solution.singleNumber(test)
print ans
