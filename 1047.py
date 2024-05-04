def kk(d):
    sta=[]
    ans=''
    for i in range(len(d)):
        if len(sta) == 0:

            sta.append(d[i])
        else:
            if sta[-1] == d[i]:
                sta.pop()
            else:
                sta.append(d[i])
    for i in sta:
        ans+=i
    return ans
print(kk('abbda'))