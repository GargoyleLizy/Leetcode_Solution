class Solution1(object):
    answ = []
    orig_nums = []
    manip_nums = []
    pre_list = []
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #self.orig_nums = list(nums)
        #self.manip_nums = nums
        pre_list = []
        self.permuteRec(pre_list,nums)
        return self.answ
    
    def permuteRec(self,pre_list,nums):
        if len(nums) == 0 :
            self.answ.append(pre_list)
            return
        else:
            for idx in range(len(nums)):
                print(idx)
                print(pre_list,nums,self.answ)
                pre_list.append(nums.pop(idx))
                self.permuteRec(pre_list,nums)
            #self.answ.append(self.pre_list)
            #self.manip_nums = list(self.orig_nums )
            #self.pre_list = []

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.wawa(nums,[],res)
        return(res)

    def wawa(self,nums,cur,res):
        print(nums,cur,res)
        if (len(nums) == 0):
            res.append(cur)
            return
        for i in range(len(nums)):
            
            nums[0],nums[i] = nums[i],nums[0]
            self.wawa(nums[1:], cur+[nums[0]], res)

test = [1,2,3]
solution = Solution()
answ = solution.permute(test)
print(answ)

