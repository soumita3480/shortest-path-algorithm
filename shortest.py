
def path(a,stack,stopx,stopy,row,col,visited):
    while stack:
        x,y=stack.pop(0)
        if x==stopx and y==stopy:
            visited[x][y]=1
            return True
        if a[x][y]==0:
            continue
        if a[x][y]==1 and visited[x][y]==1:
            continue
        if a[x][y]==1 and visited[x][y]==0:
            visited[x][y]=1
            if x-1>=0 and visited[x-1][y]==0 and a[x-1][y]==1:
                stack.append([x-1,y])
            if x+1<row and visited[x+1][y]==0 and a[x+1][y]==1:
                stack.append([x+1,y])
            if y-1>=0 and visited[x][y-1]==0 and a[x][y-1]==1:
                stack.append([x,y-1])
            if y+1<col and visited[x][y+1]==0 and a[x][y+1]==1:
                stack.append([x,y+1])
            
            
                
if __name__=='__main__':
    a=[[1, 0, 1, 1, 1 ],
        [1, 0, 1, 0,1 ],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1 ],
        [1, 1, 1, 0, 1],]

    row=5
    col=5
    visited=[[0 for _ in range(5)]for _ in range(5)]
    startx=0
    starty=0
    stopx=3
    stopy=4
    stack=[]
    stack.append([startx,starty])
    if path(a,stack,stopx,stopy,row,col,visited):
        print(visited)
        count=0
        for i in range(row):
            for j in range(col):
                print(visited[i][j],end='')
                if visited[i][j]==1:
                    count+=1
            print()
        print(count)
    else:
        print('no path found')

