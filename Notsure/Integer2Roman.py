class Solution(object): 
 
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ""
        if num / 1000 > 0 :
            M_num = num/1000
            while M_num > 0:
                ans = ans+ "M"
                M_num -= 1
            num = num % 1000
        if num / 100 > 0 :
            C_num = num/100
            if C_num == 9:
                ans = ans + "CM"
                C_num -=9
            elif C_num == 4:
                ans = ans+ "CD"
                C_num -=4
            elif C_num >= 5:
                ans = ans + "D"
                C_num -= 5

            # convert the rest of like 1~3 00, 6~800
            while C_num > 0 :
                ans = ans + "C"
                C_num -= 1
            # get the rest of number
            num = num % 100

        if num / 10 > 0 :
            X_num = num/10
            if X_num == 9:
                ans = ans + "XC"
                X_num -= 9
            elif X_num == 4:
                ans = ans + "XL"
                X_num -= 4
            elif X_num >= 5:
                ans = ans + "L"
                X_num -= 5

            while X_num > 0:
                ans = ans + "X"
                X_num -= 1
            num = num % 10

        if num == 9:
            ans = ans + "IX"
            num -= 9
        elif num == 4:
            ans = ans + "IV"
            num -= 4
        elif num >= 5:
            ans = ans + "V"
            num -= 5
        while num > 0 :
            ans = ans + "I"
            num -= 1

        return ans

solution = Solution()
test = 7
ans = solution.intToRoman(7)
print ans



