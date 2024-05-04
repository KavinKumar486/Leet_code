from collections import Counter
class Solution:
    def majorityElement(self,nums):
        f={}
        for i in nums:
            f[i]=f.get(i,0)+1
        i=max(zip(f.values(), f.keys()))[1]
        return i

d=Solution()
nums=[1,2,3,2,1,2,3,3,4,2,3,1,3]
d.majorityElement(nums)