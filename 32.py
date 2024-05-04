class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        return ((26*((len(columnTitle)-1)))+ord(columnTitle[-1])-64)
        
s=Solution()
strs='AB'
print(s.titleToNumber(strs))