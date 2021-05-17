from collections import deque
#미로 탈출

#맵 크기 입력 받기
n,m = map(int, input("맵 크기: ").split())

maps = []
for i in range(n):
    maps.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]



def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        #현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(nx<0 or nx>=n or ny<0  or ny>=m): #맵을 벗어나는 경우
                continue
            if(maps[nx][ny] == 0): #괴물이 있는 경우
                continue
            if(maps[nx][ny] == 1): #첫 방문일 때
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx,ny))

    return maps[n-1][m-1]

print(bfs(0,0))






