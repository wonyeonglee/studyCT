#음료수 얼려 먹기


#얼음틀 크기 입력 받기
n,m = map(int,input("얼음 틀  크기").split())

#얼음틀 모양 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int,input("얼음틀 모양"))))
print(graph)
def bfs(x,y):
    #얼음틀을 벗어나면
    if(x<0 or x>=n or y<0 or y>=m):
        return False
    #아직 방문하지 않았다면
    if(graph[x][y]==0):
        graph[x][y] = 1 #방문 상태로 처리하고
        #상하좌우 연결된 부분 다 check
        bfs(x,y-1)
        bfs(x,y+1)
        bfs(x-1,y)
        bfs(x+1,y)
        return True
    return False


sum=0
for i in range(n):
    for j in range(m):
        if(bfs(i,j)==True):
            sum+=1

print(sum)






