class Solution:
    def evalRpn(self,tokens):
        dic=['1','2','3','4','5','6','7','8','9','0']
        stack=[]
        for i,j in enumerate(tokens):
            if j in dic:
                stack.append(int(j))
            else:

                if j=='+':
                    stack.append(stack.pop()+stack.pop())

                elif j=='-':
                    stack.append(-1*(stack.pop()+stack.pop()))

                
                elif j=='*':
                    stack.append(stack.pop()*stack.pop())
                elif j =='/':
                    a,b=stack.pop(),stack.pop()
                    stack.append(int(b/a))
        return stack[0]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
s= Solution()
f=s.evalRpn(tokens)
print(f)