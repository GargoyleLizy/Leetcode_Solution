import sys
class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        if(int(n) ==0):
            return "1"
        elif(int(n) <= 10):
            return str(int(n)-1)
            
        firstHalf = n[:(len(n) - len(n)//2)]
        firstHalfInt = int(firstHalf)
        candidate=[]
        #construct the palidrome with first half. 
        isOddIntegers = len(n)%2 != 0
        candidate.append(self.completePalindrome(firstHalfInt,isOddIntegers))
        candidate.append(self.completePalindrome(firstHalfInt+1, isOddIntegers))
        candidate.append(self.completePalindrome(firstHalfInt-1,isOddIntegers))
        # construct the 9...9 and 10...01 numbers.
        candidate = candidate + self.constructAllNine(len(n))
        candidate = candidate + self.constructJustTwo1(len(n))
        minDistance = sys.maxsize
        original = int(n)
        ans = original
        for term in candidate:
            print(term)
            relative = abs(term - original)
            if relative!=0 :
                if relative < minDistance :
                    ans = term
                    minDistance = relative
                elif (relative == minDistance) and (term<original):
                    ans = term
                    minDistance = relative
        return str(ans)

    def completePalindrome(self, firstHalfInt, isOddIntegers):
        secondHalf = ""
        if(isOddIntegers):
            if(firstHalfInt <10):
                secondHalf = str(firstHalfInt)
            else:
                secondHalf = str(firstHalfInt//10)[::-1]
        else:
            secondHalf = str(firstHalfInt)[::-1]
        return int(str(firstHalfInt) + secondHalf)

    def constructAllNine(self, length):
        all9 = []
        if(length >= 2):
            all9.append(pow(10, length) -1)
            all9.append(10 ** (length -1)  -1)
        return all9

    def constructJustTwo1(self,length):
        justTwo1 = []
        justTwo1.append(10**length +1)
        if(length > 1):
            justTwo1.append(10 ** (length-1) +1)
        return justTwo1

test = "11"
solution = Solution()
print(solution.nearestPalindromic(test))