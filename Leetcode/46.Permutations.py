class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]

        n1 = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i+1:]
            print(n)
            for j in self.permute(n):
                # print(j)
                n1.append([num] + j)
        return n1
h = Solution()
nums = [1,2,3]
print(h.permute(nums))

# def perm(a, k=0):
#    if k == len(a):
#       print(a)
#    else:
#       for i in range(k, len(a)):
#         print(k)
#         print(a[k], a[i])
#         a[k], a[i] = a[i] ,a[k]
#         perm(a, k+1)
#         a[k], a[i] = a[i], a[k]

# perm([1,2,3])