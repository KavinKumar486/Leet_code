class Solution:
    def rearrangeArray(self, nums):
      p,n=[],[]
      for i in nums:
        if i<0:
            n.append(i)
        else:
           p.append(i)
      i=0
      while 2*i < len(nums):
         nums[2*i] = p[i]
         nums[2*i+1]=n[i]
         i+=1

      return nums
s=Solution()
nums = [3,1,-2,-5,2,-4]
f=s.rearrangeArray(nums)     
print(f)   