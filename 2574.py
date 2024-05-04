class Solution:
    def leftRightDifference(self, num):
        ans =[]
        for i in range(1,len(num)):

             
            num[i] +=num[i-1]
        print(num)
        for i in range(len(num)):
            if i ==0:
                ans.append(abs(num[0]-num[-1]))
            if i+1 >len(num)-1:
                ans.append(num[i-1])
            else:
                ans.append(abs(num[i-1]-num[i+1]))
        return ans
s=Solution()
print(s.leftRightDifference([10,4,8,3]))


