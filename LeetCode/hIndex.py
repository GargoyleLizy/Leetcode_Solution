class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        sorted_citations = sorted(citations,reverse=True)
        return self.findH(sorted_citations)


    def findH(self,sorted_citations):
        print sorted_citations
        hIndex = 0;
        if(len(sorted_citations) == 0):
            return 0
        if(sorted_citations[0] == 0):
            return 0
        for idx in range(len(sorted_citations)):
            if idx+1 > sorted_citations[idx]:
                return idx
       
        return len(sorted_citations)

test = [4,4,2,0]
solution = Solution()
print solution.hIndex(test)

