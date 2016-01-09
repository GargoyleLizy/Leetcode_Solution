class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = self.versionToInt(version1)
        version2 = self.versionToInt(version2)
        #print version1, version2
        for index in range(0,max(len(version1),len(version2))):
            try:
                elt1 = version1[index]
            except IndexError:
                elt1 = 0
            try: 
                elt2 = version2[index]
            except IndexError:
                elt2 = 0
            if elt1 > elt2 :
                return 1
            elif elt1 < elt2 :
                return -1
            
        return 0

    def versionToInt(self,version):
        
        version_split = version.split('.')
        version_new = []
        for elt in version_split:
            version_new.append(int(elt))
        return version_new

solution = Solution()
ans = solution.compareVersion('01','1.0')
print ans
