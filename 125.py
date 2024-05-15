s='AAAABBBBAAAA'
n=''
s=s.lower()
for i in s:
    if i.isalnum():
        n+=i
n= list(n)
print(n==n[::-1])