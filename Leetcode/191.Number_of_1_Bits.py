class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        # total = bin(n).count('1')
        # return total
        while n != 0:
            n &= (n-1)
            total += 1
        return total

        
h = Solution()
n = 11
print(h.hammingWeight(n))
