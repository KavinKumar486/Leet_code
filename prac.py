# class Solution:
#     def productExceptSelf(self,nums):
#         f_res=1
#         zero_ind=[]
#         l=0
#         for j,i in enumerate(nums):
#             if i !=0:
#                 f_res*=i
#             else:
#                 l+=1
#                 zero_ind.append(j)
#         if l>1:
#             return [0]*len(nums)
#         elif(l==1):
#             for i,j in enumerate(nums):
#                 if i not in zero_ind:
#                     nums[i]=0
#                 else:
#                     nums[i]=f_res
#         else:
#             for i in range(len(nums)):
#                 nums[i] = f_res//nums[i]
#         return nums
# s=Solution()
# nums = [-1,1,-3,3]
# d=s.productExceptSelf(nums)
# print(d)
                
# arr=[1,2]
# print(list(arr))
lis =[[1,2,3],[4,5,6],[7,8,9]]
res=0
for i in lis:
    res+=min(i)
print(res)