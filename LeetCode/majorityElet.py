class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        kdic = {}
        threshold_val = len(nums)/2
        for elt in nums:
            if elt in kdic:
                kdic[elt] +=1
                if kdic[elt] > threshold_val:
                    return elt
            else:
                kdic[elt] = 1
        
        for elt in kdic.keys():
            if kdic[elt] > threshold_val:
                return elt

solution = Solution()
test = [1,2,3,1,1]
ans = solution.majorityElement(test)
print ans
