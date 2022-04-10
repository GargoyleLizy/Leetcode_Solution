from  typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        resultList = self.grayCodeRec(n)
        intResultList = list(map(self.convertBitListToInt, resultList))
        return intResultList
    
    def grayCodeRec(self, n:int) -> List[List[int]]:
        if (n == 1):
            return [[0],[1]]
        if (n == 2):
            return [[0,0], [1,0], [1,1], [0,1]]
        
        results = []
        innerBitsList = self.grayCodeRec(n-2)
        innerBitsListReverse = innerBitsList.copy()
        innerBitsListReverse.reverse()
        # part 1: 0, [0, X, 0], 0 to 0, [0, X, 1], 0
        for innerBits in innerBitsList :
            item = [0] + innerBits + [0]
            results.append(item)
        # part 2: 0, [0, X, 1], 0 to 1,[0, X, 0], 0
        for innerBits in innerBitsListReverse :
            item = [1]  + innerBits + [0]
            results.append(item)
        # part 3: 1,[0, X, 0], 1 to 1, [0, X,  1], 1
        for innerBits in innerBitsList :
            item = [1] + innerBits + [1]
            results.append(item)
        # part 4: 0, [0, X,  1], 1 to 0, [0, X, 0], 1
        for innerBits in innerBitsListReverse :
            item = [0]+ innerBits + [1]
            results.append(item)
        return results

    def convertBitListToInt(self, bitsList:List[int]) -> int: 
        resultStr = ''
        for bit in bitsList :
            resultStr = resultStr + str(bit)
        return int(resultStr,2)

        
solution = Solution()
ans = solution.grayCode(3)

print(ans)
