#큰 수의 법칙
N,M,K = map(int, input("N과 M과 K입력").split()) # N: 배열 크기, M : 덧셈 횟수, K : 최대 더할 수 있는 횟수
data  = list(map(int,input().split())) #숫자 배열들

maxNum = sorted(data)[N-1] #제일 큰수
secondNum = sorted(data)[N-2] # 두번째로 큰수
k=0
sum=0
print(maxNum,secondNum)
for i in range(M):
    if(k==K):
        sum+=secondNum
        k=0
    else:
        sum+=maxNum
        k+=1

print(sum)