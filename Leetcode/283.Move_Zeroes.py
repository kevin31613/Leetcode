class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[p], nums[i] = nums[i], nums[p] 
                p += 1
        return nums

h = Solution()
nums = [0,1,0,3,12]
print(h.moveZeroes(nums))