class Solution:
    def f(self,nums):
        v=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    v+=1
            nums[i]=v
            v=0
        return nums
d = Solution()
print(d.f([6,5,4,8]))