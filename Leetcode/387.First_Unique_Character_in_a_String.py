from collections import defaultdict
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dd = defaultdict(int)
        for ss in s:
            dd[ss] += 1
        for i, ss in enumerate(s):
            if dd[ss] == 1:
                return i
        return -1

h = Solution()
s = "loveleetcode"
print(h.firstUniqChar(s))