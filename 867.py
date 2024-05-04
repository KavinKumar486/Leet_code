
# class Solution(object):
#     def transpose(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         seen=set()
#         n=len(matrix)
#         for i in range(n):
#             for j in range(n):
#                 if (i,j) not in seen:
#                     if i==j:
#                         continue
#                     matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
#                     seen.add((i,j))
#                     seen.add((j,i))
#                 else:
#                     continue
#         return matrix
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# s=Solution()
# print(s.transpose(matrix))

                

'''matrix=[[1,2,3],[4,5,6],[123,121,122]] 
for i in zip(*matrix):
    print(list(i))
temp=matrix.copy()
print(temp)
'''
class Solution:
    def arrayRankTransform(self, arr):
        temp=arr.copy()
        temp=sorted(temp)
        temp=list(set(temp))
        ans=[]
        for i in arr:
            ans.append(temp.index(i)+1)
        return ans
s=Solution()
arr =  [40,10,20,30]
a=s.arrayRankTransform(arr)
print(a)
