#볼링공 고르기
#볼링공 조합, 서로 다른 무게를 가져야한다

N,M = map(int, input().split()) #N은 볼링공 개수, M은 최대 무게
weights = list(map(int, input().split())) #무게 리스트에 넣기
#먼저 만들어 낼 수 있는 조합 개수
case = (len(weights) * (len(weights)-1))//2
#같은 무게를 가진 조합 개수
same_case = 0
for i in range(1,M+1):
    if(weights.count(i)>1): #똑같은 무게가 있으면
        same_case += (weights.count(i) * (weights.count(i)-1))//2

print(case - same_case)





