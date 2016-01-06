class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        self.genert_Rec(numRows,[],res)
        return res

    def genert_Rec(self,numRows,last,res):
        if len(last) == numRows:
            return res
        else :
            cur = [1]*(len(last)+1)
            for indx in range(len(cur)):
                if (indx == 0) or (indx == len(cur)-1):
                    cur[indx] = 1
                else:
                    cur[indx] = last[indx] + last[indx-1]
            res.append(cur)
            return self.genert_Rec(numRows,cur,res)


test = 5
solution = Solution()
ans = solution.generate(test)
for elt in ans:
    print elt
