from collections import Counter
def c(arr):
    a=Counter(arr)
    v=[]

    for i in list(a):
        v.append(a[i])
    
    if len(v)==len(set(v)):
        return True
    return False
def fg(arr):
    return (len(set(Counter(arr).values()))) == (len(Counter(arr).values()))
ar=[1,2,3,4,2,2,3,2,1,2,3,4,3,1,2,2,2,4]
print(fg(ar))