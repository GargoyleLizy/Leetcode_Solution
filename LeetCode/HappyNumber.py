class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        trans_path = set()
        if n == 1:
            return True
        else:
            trans_path.add(n)
            while n != 1:
                n = self.transform(n)
                print n , trans_path
                if n in trans_path:
                    return False
                else:
                    trans_path.add(n)
            return True


    
    def transform(self,n):
        count = 0
        for cha in str(n):
            count += int(cha)*int(cha)
        return count

solution = Solution()
test = 9
ans = solution.isHappy(test)
print ans
