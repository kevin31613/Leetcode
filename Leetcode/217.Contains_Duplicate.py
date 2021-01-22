from collections import defaultdict
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dd = defaultdict(int)
        for i in nums:
            dd[i] += 1
            if dd[i] >= 2:
                return True
        return False
h = Solution()
nums = [1,2,3,1]
print(h.containsDuplicate(nums))