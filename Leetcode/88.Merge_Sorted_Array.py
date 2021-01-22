def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    nums = list()
    nums = [n1 for i, n1 in enumerate(nums1) if i < m] + [n2 for i, n2 in enumerate(nums2) if i < n]
    l = m + n
    for i, num in enumerate(nums):
        nums1[i] = num
    for j in range(l-1):
        for k in range(l-j-1):
            if nums1[k] > nums1[k+1]:
                nums1[k], nums1[k+1] = nums1[k+1], nums1[k]
    return nums1


nums1 = []
m = 0
nums2 = [1]
n = 1
print(merge(nums1, m, nums2, n))