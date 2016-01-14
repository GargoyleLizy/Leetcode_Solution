class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]

        last_level = [0,1]
        bit_counter = 1
        while bit_counter != n:
            base_numb = 1 << bit_counter
            last_length = len(last_level)
            for index in range(0,last_length):
                #print last_length - index
                last_level.append( base_numb | last_level[last_length-index -1] )
            bit_counter += 1
        return last_level

solution = Solution()
ans = solution.grayCode(1)
print ans
