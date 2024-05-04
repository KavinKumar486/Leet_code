def reg(act,reg):
    pt1=0
    pt2=0
    temp=''
    i=0
    while pt1<len(act)-1 :
        if act[pt1] == reg[pt2]:
            temp= reg[pt2]
            pt1+=1
            pt2+=1
            
        elif reg[pt2] =='*':
            
            while act[pt1] == temp and pt1<len(act)-1:
                print(act[pt1+1])
                
                pt1+=1
        elif reg[pt2] == '.':
            
            temp = act[pt1]
            pt1+=1
            pt2+=1
        else:
            return False
        print(pt1,pt2)
    return True
print(reg('aaaml','.*'))
