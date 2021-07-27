#동전 0 (백준 알고리즘 문제)

    n, k = map(int, input().split()) #n은 동전 종류, k는 만들어야 하는 합계
    coins = []
    index = -1
    sum = 0  #동전 개
    for i in range(n):
        coin = int(input())
        coins.append(coin) #동전을 입력받는다
        if(k<coin and index==-1):#커지는 순간 그 인덱스
            index = (i-1)
    for j in range(index,-1,-1):
        sum += (k//coins[j])
        k = k %coins[j]
        if(k==0):
            break
    print(sum)


