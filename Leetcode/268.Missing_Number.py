class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)+1):
            if i != nums[i]:
                return i
        # n1 = [i for i in range(len(nums)+1)]
        # for n2 in n1:
        #     if n2 not in nums:
        #         return n2
nums = [0,1]
h = Solution()
print(h.missingNumber(nums))