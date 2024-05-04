l=[[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
s={}
for i in l:
    if i[0] not in s:
        s[i[0]]=0
    if i[1] not in s:
        s[i[1]]=0

for i in l:

    if i[1] in s:
        s[i[1]]+=1
l1=[]
l2=[]
for i in s:
    
    
    if s[i] == 0:
        l1.append(i)
    if s[i] == 1:
        l2.append(i)
        
ans=[]
ans.append(sorted(l1))
ans.append(sorted(l2))


print(s)
print(ans)
