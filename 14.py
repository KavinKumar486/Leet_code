s='aaaabbb'
l=0
r=len(s)-1
res=0
while l<r:
    if s[l] == s[r]:
        r-=1
        l+=1
    else:
        res+=1
        l+=1
res1= 0
l=0
r=len(s)-1
while l<r:
    if s[l] == s[r]:
        r-=1
        l+=1
    else:
        res1+=1
        r-=1
print(min(res,res1))
