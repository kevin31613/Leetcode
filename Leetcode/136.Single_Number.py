from collections import defaultdict
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # s1 = {}
        # for i in nums:
        #     s1[i] = s1.get(i,0) + 1
        # for i in nums:
        #     if s1.get(i,0) == 1:return i
        s1 = defaultdict(int)
        for i in nums:
            s1[i] += 1
        for ss in s1:
            if s1[ss] == 1:return i

nums = [4,0,4]
h = Solution()
print(h.singleNumber(nums))