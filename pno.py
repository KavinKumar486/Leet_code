def lands(grid):
    temp=[]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c]==1:
                temp.append(bfs(r,c))
                
    return  temp
def bfs(start_x,start_y):
    end_x=start_x
    end_y= start_y
    while start_x <len(grid) and grid[start_x][end_x] ==1:
        start_y = start_x
        while end_y<len(grid[0]) and grid[start_y][end_y] == 1:
            grid[start_y][end_y] =0 
            end_y +=1
        start_x+=1
        

    return [start_x,end_x,start_y,end_y] 
grid =[[1,1,0,0],[1,1,0,1],[1,1,0,0]]
print(lands(grid))
print(grid)