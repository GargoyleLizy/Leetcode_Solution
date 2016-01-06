class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if(len(gas) == 0):
            return -1
        else:
            answ = -1
            for idx in range(len(gas)):
                if(gas[idx] >= cost[idx]):
                    answ = self.testNode(idx,self.increCur(idx,len(gas)),gas[idx]-cost[idx],gas,cost)
                    if answ != -1:
                        return answ+1
            return answ

    def testNode(self,det,cur,amout,gas,cost):
        #print(det,cur,amout,gas,cost)
        if(det != cur):
            if(amout + gas[cur] >= cost[cur]):
                cur = self.increCur(cur,len(gas))
                amout = amout+gas[cur] - cost[cur]
                return self.testNode(det,cur,amout,gas,cost)
            else:
                return -1
        else:
            return det
    
    def increCur(self,cur,gas):
        if(cur+1 == gas):
            return 0
        else:
            return cur+1

gas = [4]
cost = [5]
solution = Solution()
answ = solution.canCompleteCircuit(gas,cost)
print(answ)
