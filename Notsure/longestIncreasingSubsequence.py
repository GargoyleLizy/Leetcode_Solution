class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        else:
            default = nums[0]
            length = 0
            record = 0
        for elt in nums:
            if elt >= default:
                length +=1
            else:
                if length > record:
                    record = length
                length = 1
            default = elt
        return max(length,record)


test = [1,2,3,2]
solution = Solution()
ans = solution.lengthOfLIS(test)
print ans
