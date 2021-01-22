num = 9996

nums = str(num)
nums2 = []
maxnum = num
for i, nn  in enumerate(nums):
    if nn == '6':
        nn = '9'
    else:
        nn = '6'
    nums2 = nums[:i] + nn + nums[i+1:]
    if maxnum < int(nums2):
        maxnum = int(nums2)
print(maxnum)