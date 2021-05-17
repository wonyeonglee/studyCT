#상하좌우

dir = ['L','R','U','D'] #갈 수 있는 방향
dy = [-1,1,0,0]
dx = [0,0,-1,1]

x = 1 #초기 위치
y = 1 #초기 위치

n = int(input("공간 크기 입력: "))
plans = list(map(str, input("여행계획").split())) #여행 계획 배열

for plan in plans: #플랜 별로
    for i in range(len(dir)): #방향 check
        if(plan==dir[i]): #방향이 맞으면
            if(x+dx[i]>=1 and y+dy[i]<=n): #공간을 벗어 나지 않으면 이동
                x= x+dx[i] #방향 맞게 이동
                y =y+dy[i] #방향 맞게 이동
print(x, y)
