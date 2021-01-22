class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        total = 0
        s1 = {}
        for i in A:
           for j in B:
                s1[i+j] = s1.get(i+j,0) + 1
        # print(s1)
        for i2 in C:
            for j2 in D:
                # print(s1.get(-(i2+j2)))
                total += s1.get(-(i2+j2),0)
        return total



# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
A = [-1,-1]
B = [-1,1]
C = [-1,1]
D = [1,-1]
# B = [0]
# C = [0]
# D = [0]
h = Solution()
print(h.fourSumCount(A, B, C, D))  