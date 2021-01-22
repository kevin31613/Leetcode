class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        nums2 = list()
        for i in range(n):
            nums2.append(nums[i])
            nums2.append(nums[i+n])
        return nums2


nums = [1,2,3,4,4,3,2,1]
n = 4
h = Solution()
print(h.shuffle(nums, n))
