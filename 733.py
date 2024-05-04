class Solution:
    def floodFill(image, sr, sc, color):
        def dfs(row,col,sr,sc,image,color,src):
            if sr<0 or sc<0 or sc>=col or sr>=row:
                return
            elif(image[sr][sc]!=src):
                return
            image[sr][sc]=color
            dfs(row,col,sr,sc-1,image,color,src)
            dfs(row,col,sr,sc+1,image,color,src)
            dfs(row,col,sr+1,sc,image,color,src)
            dfs(row,col,sr-1,sc,image,color,src)
        row = len(image)
        col=len(image[0])
        src=image[sr][sc]
        dfs(row,col,sr,sc,image,color,src)
        return image
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
print(Solution.floodFill(image,sr,sc,color))