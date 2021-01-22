class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        dd = {}
        dd['I'] = 1
        dd['V'] = 5
        dd['X'] = 10
        dd['L'] = 50
        dd['C'] = 100
        dd['D'] = 500
        dd['M'] = 1000
        for i in range(len(s)-1):
            if dd.get(s[i]) >= dd.get(s[i+1]):
                total += dd.get(s[i])
            else:
                total -= dd.get(s[i])
        total += dd.get(s[-1])
        return total 
h = Solution()
s = "IV"
print(h.romanToInt(s))
