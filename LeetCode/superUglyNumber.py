class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 1:
            return 1
        else:
            result = [1];
            founds_ugly = 1
            prime_index = [0] * len(primes)
            while founds_ugly != n:
                next_nums = []
                for index in range(len(primes) ):
                    next_nums.append(primes[index]*result[prime_index[index]])
                min_result = min(next_nums)
                result.append(min_result)

                for index in range(len(primes)):
                    if primes[index]*result[prime_index[index]] == min_result:
                        prime_index[index] +=1

                founds_ugly += 1

            return result[-1]

solution = Solution()
test = [2,3,5]
ans = solution.nthSuperUglyNumber(3,test)
print ans
        
