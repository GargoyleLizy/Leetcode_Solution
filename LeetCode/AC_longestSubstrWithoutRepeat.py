
class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        cur = set()
        for cha in s:
            if cha in cur:
                if len(cur) > ans:
                    ans = len(cur)
                cur = set()
                cur.add(cha)
            else:
                cur.add(cha)

        if len(cur) > ans:
            return len(cur)
        else:
            return ans

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        cur = ''
        for cha in s:
            #print cur
            if cha in cur:
                #update current string
                cur = cur.split(cha)[1]+cha
                if len(cur) > ans:
                    ans = len(cur)
            else:
                cur += cha
                if len(cur) > ans:
                    ans = len(cur)
        

        
        return ans


test = 'ancddd'
solution= Solution()
ans = solution.lengthOfLongestSubstring(test)
print ans

