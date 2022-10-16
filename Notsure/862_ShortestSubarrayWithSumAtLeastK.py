class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if(len(A) == 0):
            return -1
        if(len(A) == 1):
            if(A[0] >= K):
                return 1
            else:
                return -1
        
        currentMin = len(A)+1
        headIndex = 0
        tailIndex = 0
        currentSum = A[0]
        currentSize = 1

        while(not(tailIndex == len(A)-1 and headIndex == len(A)-1)):
            #print(""+str(headIndex) + ":" +str(tailIndex) + "=" + str(currentSum) + ";" + str(currentMin))
            if(currentSum>=K):
                currentMin = min(currentMin,currentSize)
            if(headIndex==len(A)-1):
                currentSum -= A[tailIndex]
                tailIndex+=1
                currentSize-=1
                if(currentSum>=K):
                    currentMin = min(currentMin,currentSize)
            else:
                if(currentSum < K):
                    negativeOrZeroHeadIndex = self.subArrayNegativeOrZeroHeadIndex(A,tailIndex,headIndex)
                    if(negativeOrZeroHeadIndex!= None):
                        currentSum -= negativeOrZeroHeadIndex[1]
                        currentSize -= (negativeOrZeroHeadIndex[0] - tailIndex) +1
                        tailIndex = negativeOrZeroHeadIndex[0]+1
                    else:
                        headIndex+=1
                        currentSum += A[headIndex]
                        currentSize+=1
                else:
                    if(currentSize>1):
                        currentSum -= A[tailIndex]
                        tailIndex+=1
                        currentSize-=1
                    else:
                        headIndex+=1
                        currentSum += A[headIndex]
                        currentSize+=1
        
        if(currentMin == len(A)+1):
            return -1
        else:
            return currentMin
    
    def subArrayNegativeOrZeroHeadIndex(self,A,tailIndex,headIndex):
        currentSum =0
        for i in range(tailIndex,headIndex):
            currentSum+= A[i]
            if(currentSum <= 0):
                return (i,currentSum)
        return None




solution = Solution()
A= [-34,37,51,3,-12,-50,51,100,-47,99,34,14,-13,89,31,-14,-44,23,-38,6]
K =151
ans = solution.shortestSubarray(A,K)
print(ans)