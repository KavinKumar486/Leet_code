def f(f):
    d = {'I':1,'V':5,'X':10,'C':100,'L':50,'D':500,'M':1000}
    f=list(f)
    s=0
    st=0
    if len(f) == 1:
        return s+d[f[0]]
    while st < len(f)-1:

        if d[f[st]]>=d[f[st+1]]:
            print(d[f[st]],d[f[st+1]])
            s+=d[f[st]]
            st+=1
        else:
            s+=d[f[st+1]]-d[f[st]]
            st+=2
    if st == len(f)-1:
        s+= d[f[st+1]]
    return s
print(f('II'))