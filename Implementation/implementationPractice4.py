#게임 개발

n,m = map(int, input("맵크기 n* m: ").split()) #맵 크기 입력받기
a,b,d = map(int, input("위치와 방향: ").split())

map = []
for i in range(m):
    input_data = list(map(int, input(i,"번째줄:").split()))
    map.append(input_data)

directions = [0,1,2,3] #갈 수 있는 방향 북,동,남,서
dA = [-1,0,1,0] #방향 인덱스에 맞게 이동
dB = [0,1,0,-1] #방향 인덱스에 맞게 이동
sum=0
turn_time = 0 #같은 자리에서 방향 돌린 횟수
while True:
    #일단 현재 위치를 1로 바꾼다 (가본 곳이기 때문에)
    map[a][b] = 1
    d = d-1 #현재 방향에서 왼쪽 방향을 본다
    if(d==-1): #현재 방향이 북이면
        d = 3
    for i in len(directions): #방향 검사
        if(d==directions[i]): #해당 방향이면
            #이동하는 곳 계산해서 바다가 아니고, 이전에 가보지 않은 곳이라면..
            if(map[dA+a][dB+b]!=1):
                sum+=1
                map[dB+b][dA+a]=1
                a = dA+a
                b = dB+b
                turn_time=0
            else:
                turn_time +=1

            if(turn_time==4): #모든 방향에 갈 자리가 없다면
                #한칸 뒤로 간다
                if(a-dA[i]):






