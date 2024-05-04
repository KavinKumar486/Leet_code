class Solution:
    def islandPerimeter(self, grid):
        r,c=0,0
        row,col=len(grid),len(grid[0])
        for j,i in enumerate(grid):
            if 1 in i:
                r,c=j,i.index(1)
                break
        tot=4
        visited = set()
        def dfs(r,c,tot,visited):
            if (r,c) in visited:
                return
            visited.add((r,c))
            if (r>row-1 or r<0 or c>col-1 or c<0):
                return 
            if grid[r][c] ==0 :
                return 
            else:
                tot+=2

            
            dfs(r+1,c,tot,visited)
            dfs(r-1,c,tot,visited)
            dfs(r,c+1,tot,visited)
            dfs(r,c-1,tot,visited)
            return tot
        dfs(r,c,tot,visited)
            
        
        return tot
grid=[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
s=Solution()
r=s.islandPerimeter(grid)
print(r)