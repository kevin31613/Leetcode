
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    h = {}
    for i, num in enumerate(nums):
        n = target - num
        if n not in h:
            h[num] = i
        else:
            print(h)
            return [h[n], i]

nums = [2,11,7,15]
target = 9
print(twoSum(nums, target))
