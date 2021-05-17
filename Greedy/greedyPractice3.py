#숫자 카드 게임

n,m = map(int,input("입력 : ").split())
ex_min = 0
for i in range(n):
    data = list(map(int,input().split())) #한 줄
    minNum = sorted(data)[0]
    minNum = max(ex_min,minNum) #가장 작은 수 들 중에서 큰 수 찾기

print(minNum)

