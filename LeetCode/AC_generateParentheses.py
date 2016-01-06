class Solution(object):
    start_p = '('
    end_p = ')'
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.gp_rec(0,n,'',res)
        return res

    def gp_rec(self,pre_open,left,cur,res):
        if((left==0) & (pre_open ==0)):
            cur+= ''
            res.append(cur)
            return
        elif((left > 0) & (pre_open==0)):
            cur+=self.start_p
            self.gp_rec(1,left-1,cur,res)
        elif((left==0) & (pre_open >0)):
            cur+= self.end_p
            self.gp_rec(pre_open-1,0,cur,res)
        elif((left>0)&(pre_open>0)):
            cur1 = cur+self.start_p
            self.gp_rec(pre_open+1,left-1,cur1,res)
            cur2 = cur+self.end_p
            self.gp_rec(pre_open-1,left,cur2,res)

solution = Solution()
ans = solution.generateParenthesis(3)
print(ans)
