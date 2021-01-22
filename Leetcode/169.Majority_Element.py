from collections import defaultdict

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = defaultdict(int)
        for i in nums:
            n[i] += 1
        l = len(nums)
        for i in nums:
            if n[i] > l/2:
                return i

nums = [4,0,4]
h = Solution()
print(h.majorityElement(nums))