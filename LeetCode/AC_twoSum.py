class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsD = self.toDict(nums,target)
        for idx in range(len(nums)):
            diff = target - nums[idx]
            #print(idx,diff)
            if ( diff in numsD):
                if ( numsD[diff] != idx+1):
                    return [idx+1,numsD[diff]]

    def toDict(self,nums,target):
        numsD = {}
        for idx in range(len(nums)):
            #if nums[idx] <= target:
            numsD[nums[idx]] = idx+1
        return numsD

test = [-3,4,3,2,4]
target = 0
test = [-1,-2,-3,-4,-5]
target = -8
solution = Solution()
ans = solution.twoSum(test,target)

print(ans)
