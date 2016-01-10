class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        match_index = 0
        for index in range(0,len(haystack) ):
            if haystack[index] != needle[match_index]: 
                pass
            else:
                #print haystack[index:index + len(needle)]
                if haystack[index:index + len(needle)] == needle:
                    return index
        return -1

solution = Solution()
haystack = "misissip"
needle = "issip"
ans = solution.strStr(haystack,needle)
print ans




