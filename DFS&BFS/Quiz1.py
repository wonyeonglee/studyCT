#특정 거리의 도시 찾기 p.339

#도시의 개수 n, 도로의 개수 : M, 거리 정보 K, 출발 도시 번호 x
INF = 999999
from collections import deque
n,m,k,x = map(int, input().split())
#2차원 배열
graph = [[ INF for col in range(n+1)]  for row in range(n+1)]

distance = [INF]* (n+1) #거리 초기화
distance[x] = 0 #출발 노드는 0으로

print(distance)
for mm in range(m): #거리입력받
    i,j = map(int, input().split())
    graph[i][j] = 1

queue = deque([x]) #큐 생성 x가 들어가있는

while(queue):#q가 빌때까지
    city = queue.popleft()#도시를 빼온다  지금 1번 도시
    print(city)
    dis = distance[city]  #현재 city까지의 거리
    print(dis)
    for i in range(1,n+1): #city와 연결된 모든 도시 탐
        if (graph[city][i] !=INF): #연결됐으
            if(i not in queue):
                queue.append(i)
                distance[i] = min(graph[city][i],graph[city][i] + dis)
    print("-------")
print(distance)





