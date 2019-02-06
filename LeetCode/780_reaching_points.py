class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        # inputs will be equal or greater than 1.
        # handle 
        print tx, ty
        if(tx<sx or ty < sy):
            return False
        if(sx == tx and sy == ty):
            return True
        if(tx < ty ):
            if(tx == sx):
                if( (ty -sy) % tx == 0) :
                    return True
                else:
                    return False
            else:
                return self.reachingPoints(sx,sy,tx,ty%tx )
        else :
            if(ty == sy):
                if((tx-sx) % ty ==0):
                    return True
                else: 
                    return False
            else:
                return self.reachingPoints(sx,sy,tx%ty,ty)


solution = Solution()
print(solution.reachingPoints(3,3,12,9) )