class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numsD = {}
        for indx in range(len(nums) ):
            if nums[indx] in numsD:
                if ( indx - numsD[nums[indx]] ) <= k:
                    return True
                else:
                    numsD[nums[indx]] = indx
            else:
                numsD[nums[indx]] = indx
        return False


test = [1,2,3,1,3]
solution = Solution()
ans = solution.containsNearbyDuplicate(test,2)
print ans
