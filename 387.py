from collections import Counter
class Solution:
    def findUniqChar(self,s):
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        for i in s:
            if d[i]==1:
                return i
        return (-1)
s=Solution()
f='eettccooddee'
a=s.findUniqChar(f)
print(a)