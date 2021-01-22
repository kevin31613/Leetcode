class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        h = []
        while 1:
            s = 0
            while n > 0:
                s += (n % 10)**2
                n //= 10
            if s == 1:
                return True
            if s in h:
                return False
            else:
                h.append(s)
                n = s

h = Solution()
n = 19
print(h.isHappy(n))