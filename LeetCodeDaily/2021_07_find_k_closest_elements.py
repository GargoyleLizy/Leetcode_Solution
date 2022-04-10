from typing import List, Tuple

class Solution:
    
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # k == 0
        if k==0 : 
            return []
        if x <= arr[0]: 
            return arr[0:k]
        if x >= arr[-1]:
            return arr[len(x)-k:len(x)]
        
        return []
    
    def findClosestIndex(self, arr:List[int], x:int) -> int:
        startPos = 0
        endPos = 0
        for idx, element in arr :
            if element == x:
                 startPos = idx
                 endPos = idx
                 return (startPos, endPos)
            if element < x: 
                startPos = idx
            if element > x:
                endPos = idx
                closestPos = self.compareCloserIndex(arr, startPos, endPos, x)
                return closestPos

    def compareCloserIndex(self, arr:List[int], lowerPos:int, higherPos:int, x:int) -> int :
        if abs(x-arr[lowerPos]) < abs(x-arr[higherPos]):
            return lowerPos
        if abs(x-arr[lowerPos]) > abs(x-arr[higherPos]):
            return higherPos
        return lowerPos

    def expandStartEndPos(self, arr:List[int], k:int, x:int, closestPos:int) -> List[int] :
        if k==1:
            return [arr[closestPos]]
        n = k-1 
        startPos = closestPos
        endPos = closestPos
        while n > 0:
            if startPos == 0:
                return arr[0:k]
            if endPos == len(arr)-1:
                return arr[len(x)-k:len(x)]
            
        
                
    
    

solution = Solution()