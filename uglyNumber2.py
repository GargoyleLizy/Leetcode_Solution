class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        num = 1
        while(True):
            if(count != n):
                #print(count,num)
                if(self.isUgly(num)):
                    count=count+1
                    num+=1
                else:
                    num+=1
            else:
                break
        return num-1
        
    def isUgly(self,num):
        if(num > 1):
            if(num%2==0 ):
                
                num = num/2
                #print(num)
                return self.isUgly(num)
            elif(num%3==0):
                num = num/3
                return self.isUgly(num)
            elif(num%5 == 0):
                num=num/5
                return self.isUgly(num)
            else:
                return False
        elif(num==1):
            return True

test = 10
solution = Solution()
print(solution.nthUglyNumber(246) )
#solution.nthUglyNumber(test)
