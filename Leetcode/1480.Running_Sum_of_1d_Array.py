class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        nums1 = list()
        nums2 = list()
        k = 0
        h = 0
        while k < l:
            k += 1
            nums1 = [n1 for i, n1 in enumerate(nums) if i < k]
            h = sum(nums1)
            nums2.append(h)
        print(nums2)

nums = [1,2,3,4]
h = Solution()
print(h.runningSum(nums))       