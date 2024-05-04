
class Solution:
    def minimumLength(self, s: str) -> int:
        l=len(s)
        if l == 1:
            return 1
        pt1=0
        pt2=l-1
    
        while pt1<=pt2 and pt1<len(s)-1 and pt2>0:
            if s[pt1]==s[pt2]:
                while s[pt1] == s[pt2]:
                    pt1+=1
                while s[pt1-1]==s[pt2]:
                    pt2-=1
            else:
                break
                


        return (pt2-pt1+1) if pt1<pt2 else 0
d= Solution()
s = "cac"
g=d.minimumLength(s)
print(g)