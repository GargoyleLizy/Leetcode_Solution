class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secret_str = str(secret)
        guess_str = str(guess)
        bulls_count,secret_str,guess_str = self.getBulls(secret_str,guess_str)
        cows_count = self.getCows(secret_str,guess_str)
        return ''.join([str(bulls_count),'A',str(cows_count),'B'])

    def getBulls(self,secret_str,guess_str):
        bulls_indx = []
        print('orig:',secret_str,guess_str)
        for idx in range(len(secret_str  )):
            if(secret_str[idx] == guess_str[idx]):
                bulls_indx.append(idx)
                
        # remove the bulls
        #for elt in bulls_str:
        #    secret_str = secret_str.replace(elt,'')
        #    guess_str = guess_str.replace(elt,'')
        for idx in range(len(bulls_indx)):
            cha_str_idx = bulls_indx[idx] - idx
            secret_str = secret_str[:cha_str_idx] + secret_str[cha_str_idx+1:]
            guess_str = guess_str[:cha_str_idx] + guess_str[cha_str_idx+1:]

        print(bulls_indx,secret_str,guess_str)
        return len(bulls_indx),secret_str,guess_str

    def getCows(self,secret_str,guess_str):
        cows_str = ''
        print(secret_str,guess_str)
        for idx in range(len(secret_str)) :
            for idx2 in range(len(guess_str)):
                if guess_str[idx2] == secret_str[idx]:
                    cows_str += guess_str[idx2]
                    guess_str = guess_str[:idx2] + guess_str[idx2+1:]
                    break
                    
        print(cows_str)
        return len(cows_str)

test1 = 1122
test2 = 2211
solution= Solution()
print solution.getHint(test1,test2)


