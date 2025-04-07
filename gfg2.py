
class Solution:
    def isBalanced(self, s):
        # code here
        freq={')':'(','}':'{',']':'['}
        stack=[]
        for i in s:
            if not stack:
                stack.append(i)
                continue
            if i in freq:
                print(stack)
                if stack[-1] != freq[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        print(stack)
        return len(stack)==0
s = Solution()
j='[{()}]'
print(s.isBalanced(j))
