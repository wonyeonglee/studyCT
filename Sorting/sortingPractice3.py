#두 배열의 원소 교체
n,k = map(int, input("n과 k : ").split()) #n,k입력 받기 n:배열 크기 k: 연산 수행 횟수

a = list(map(int, input("a배열").split())) #a배열
b = list(map(int, input("b배열").split())) #b배열

for i in range(k): #바꿔치기 연산 수행 (k번)
    #a배열에서 제일 작은 수 선택
    a.sort()
    b.sort()
    #b배열에서 제일 큰 수 선택
    if(a[0]<b[n-1]): #a에서 젤 작은 수가 b에서 젤 큰수 보다 작아야만 change
        a[0],b[n-1] = b[n-1],a[0]
sum=0
for num in a:
    sum+=num
print(sum)


