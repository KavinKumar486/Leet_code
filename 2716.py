class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1=version1.split('.')
        version2= version2.split('.')
        for j,i in enumerate(version1):
            version1[j] = int(i)
        for j,i in enumerate(version2):
            version2[j] = int(i)
        
        l= abs(len(version1) - len(version2))
        if len(version1)>len(version2):
            for i in range(l):
                version2.append(0)
        elif (len(version1)<len(version2)):
            for i in range(l):
                version2.append(0)
        print(version1,version2)
        for i,j in zip(version1,version2):
            if i>j:
                return 1
            elif(j>i):
                return -1
        return 0
ver='1'
ver1='1.1'
s=Solution()
p=s.compareVersion(ver,ver1)
print(p)
