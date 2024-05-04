class Solution(object):
    def threeSum(self, nums):
        nums=list(set(nums))
        nums.sort()
        ans=[]
        for i,j in enumerate(nums):
            l=i
            r=len(nums)-1
            
            while l<r:
                if nums[l]+nums[r]+j > 0:
                    r-=1
                elif nums[l]+nums[r]+j < 0:
                    l+=1
                else:
                    ans.append([nums[l],nums[r],j])
                    l+=1
                    while l<r and l < len(nums):
                        l+=1
        return ans

nums=[-1,0,1,2,-1,-4,3,1,-1,-1,2,9,-1,-8]
s=Solution()
f=s.threeSum(nums)
print(f)