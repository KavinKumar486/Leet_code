'''def g(strs):
    pt1 =0
    pt2 = float('inf')
    i=0
    while i<len(strs):
        for j in range (len(strs)):
            if strs[i][j]:
                pt1+=1
                
            else: 
                break
    
        i+=1
        pt2= min(pt1,pt2)
        pt1=0
    
    return(strs[0][:pt2])
a=g(['flowei','flower'])
print(a)
'''
