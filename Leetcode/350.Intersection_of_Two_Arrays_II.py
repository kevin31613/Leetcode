class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums3 = []
        for nn in nums1:
            if nn in nums2 and nn not in nums3:
                min1 = nums1.count(nn)
                min2 = nums2.count(nn)
                if min1 == min2:
                    for j in range(min1):
                        nums3.append(nn)
                elif min1 < min2:
                    for j in range(min1):
                        nums3.append(nn)
                else:
                    for j in range(min2):
                        nums3.append(nn)
        return nums3
h = Solution()
nums1 = [1,2,2,1]
nums2 = [1]
print(h.intersect(nums1, nums2))