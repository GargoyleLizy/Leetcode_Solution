class Solution(object):
    romanIntDict = {
              "I":1
            , "V":5
            , "X":10
            , "L":50
            , "C":100
            , "D":500
            , "M":1000
            , "IV":4
            , "IX":9
            , "XL":40
            , "XC":90
            , "CD":400
            , "CM":900
            }
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s != "":
            ans = self.romanToIntRec(s,0)
        else:
            ans = 0
        return ans
    
    def romanToIntRec(self,s,count):
        if s == "":
            return count
        elif len(s) >= 2:
            if s[:2] in self.romanIntDict.keys():
                count += self.romanIntDict[s[:2]]
                return self.romanToIntRec(s[2:],count)
            else:
                count += self.romanIntDict[s[:1]]
                return self.romanToIntRec(s[1:],count)
        else:
            count += self.romanIntDict[s[:1]]
            return self.romanToIntRec(s[1:],count)

solution = Solution()
test = "XIX"
ans = solution.romanToInt(test)
print ans
 

