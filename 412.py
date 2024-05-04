def fizzBuzz(n):
    k=""
    ans=[]
    for i in range(1,n+1):
        if i%3 ==0:
            k+="Fizz"
        if i%5 == 0:
            k+="Buzz"
        if i%3 !=0 and i%5 != 0:
            k+=str(i)
        ans.append(k)
        k=''
    return ans
            
print(fizzBuzz(15))