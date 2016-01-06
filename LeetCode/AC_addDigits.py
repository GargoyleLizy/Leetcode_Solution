class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num > 9:
            num_str = str(num)
            str_sum = 0
            for cha in num_str:
                str_sum += int(cha)
            return self.addDigits(str_sum)
        else:
            return num

solution = Solution()
test = 38
ans = solution.addDigits(38)
print ans
