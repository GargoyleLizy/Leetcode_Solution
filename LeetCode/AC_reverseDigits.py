class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <0:
            return -1* self.reverse(-1*x)
        else:
            ans_str = ''
            x_str = str(x)
            for cha in x_str:
                ans_str = cha + ans_str
            ans =  int(ans_str)
            if (ans > 2**31) or (ans <= -1*2**31):
                return 0
            else:
                return ans

test = -123
solution = Solution()
ans = solution.reverse(test)
print ans
