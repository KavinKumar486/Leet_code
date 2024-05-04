class Solution:
    def mostFrequentEven(self, nums):

        h={}
        mx = float('-inf')
        idx=float('inf')
        if not nums:
            return -1
        for i in nums:
            if i%2 ==0:
                h[i]=h.get(i,0)+1
                
        for i,j in h.items():
            if mx<=j:
                print('e')
                if i<idx:
                    idx= i
                mx = j

        print(h,mx)

        if not h:
            return -1
        
        return idx
s=Solution()
p=s.mostFrequentEven([0,0,1,2,3,4,2,5,6,7,5,2])
print(p)


        

