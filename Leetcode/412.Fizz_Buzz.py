class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        s = []
        for i in range(n):
            if (i+1) % 3 == 0 and (i+1) % 5 == 0 and i+1 > 0:
                s.append('FizzBuzz')
            elif (i+1) % 3 == 0:
                s.append('Fizz')
            elif (i+1) % 5 == 0:
                s.append('Buzz')
            else:
                s.append(str(i+1))
        return s
n = 15      
h = Solution()
print(h.fizzBuzz(n)) 