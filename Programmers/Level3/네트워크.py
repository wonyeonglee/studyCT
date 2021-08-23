#테스트 케이스에선 양방향 그래프로 안 주는것 같다..
#
#
#
def dfs(computers, v, visited):
    visited[v] = True #방문 처리 해주고
    print(visited)
    #v와 연결되어 있는 애들 중 방문 안한 애
    for i in range(len(computers)):
        if(visited[i] == False and (computers[v][i] ==1 or computers[i][v]==1)):
            #방문안했고 연결이 되어 있을 때
            dfs(computers,i,visited)
            return True
    return True
def solution(n, computers):
    print(computers)
    for i in range(len(computers)):
        for j in range(len(computers)):
            if(computers[i][j] == 1):
                computers[j][i] =1
    print(computers)
    answer = 0
    #n : 컴퓨터 개수
    #computers = 연결에 대한 정보 2차원 배열
    #네트워크의 개수
    visited = [False] * n #방문 정보
    for i in range(n): #모든 애들 방문
        if(visited[i] == False):#방문 안한 애들 탐색
            dfs(computers,i,visited)
            answer+=1
    return answer
print(solution(4,[[1,0,0,1], [0,1,1,0],[0,1,1,0],[0,1,1,0]]))