''' def cas(f):
    if f==1:
        return '1'
    ans = cas(f-1)
    print(ans)
    count =0
    answ=''
    
    st =0
    c=1
    ele = 0
    while st < len(ans):
##        if st < len(ans)-1:
        
        
            while len(ans) >1:
                c+=1
                st+=1
                if st+1 <= len(ans):
                    
                    break
            
        
            
        c=str(c)
        st+=1
        answ = c+ans[ele]
        ele+=int(c)        
    return answ
a=cas(4)
print(a)
 '''       
        
        
        
            
